from collections import Counter
n = int(input())


def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


S = str2intWithArray(list(input()))

W = list(map(int, input().split()))
cW = Counter(W)

ans = sum(S)
now = sum(S)

dic = {}
for i in range(n):
    if not W[i] in dic:
        dic[W[i]] = 0
    dic[W[i]] = dic[W[i]] + 1 if S[i] == 1 else dic[W[i]] - 1

dicKeys = sorted(list(dic.keys()))


for i, dicKey in enumerate(dicKeys):
    now = now - dic[dicKey]
    ans = max(now, ans)

print(ans)
