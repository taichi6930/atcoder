from copy import deepcopy


def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


h, w, k = map(int, input().split())
C = [str2intWithArray(list(input().replace('#', '1').replace('.', '0')))
     for _ in range(h)]

hLists, wLists = [], []

for i in range(2 ** h):
    lis = [False] * h
    for j in range(h):
        lis[j] = i >> j & 1 == True
    hLists.append(list(lis))

for i in range(2 ** w):
    lis = [False] * w
    for j in range(w):
        lis[j] = i >> j & 1 == True
    wLists.append(list(lis))

ans = 0

for hList in hLists:
    for wList in wLists:
        c = deepcopy(C)
        for i, hbool in enumerate(hList):
            for j, wbool in enumerate(wList):
                if not(hbool or wbool):
                    continue
                for a in range(w):
                    c[i][j] = 0
        ans += 1 if sum([sum(d) for d in c]) == k else 0

print(ans)
