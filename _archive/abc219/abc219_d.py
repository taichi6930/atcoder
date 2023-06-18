# n = 1000
# x, y = 5000, 5000
# AB = [[i, i] for i in range(n)][::-1]

from pprint import pprint
n = int(input())
x, y = map(int, input().split())

AB = sorted([list(map(int, input().split())) for _ in range(n)], reverse=True)

lis = {1: []}
lis[0] = [[0, 0]]
ans = n
swi = False
cnt = 1

for i, [a, b] in enumerate(AB):
    for j in range(min(i + 1, ans)):
        li = lis[j]
        for l in li:
            if [l[0] + a, l[1] + b] in lis[j + 1]:
                continue
            if l[0] + a < x or l[1] + b < y:
                lis[j + 1].append([l[0] + a, l[1] + b])
                continue
            ans = min(ans, j + 1)
            swi = True
    for j in range(min(i + 1, ans)):
        li = sorted(lis[j])
        lenlis = len(li)
        newLi = [li[0]]
        for k in range(1, lenlis):
            swi2 = True
            for nl in newLi:
                if nl[0] <= li[k][0] and nl[1] <= li[k][1]:
                    swi2 = False
                    break
            if swi2:
                newLi.append(li[k])
        lis[j] = newLi
    for q in range(1, cnt + 1):
        if len(lis[q]) <= 1:
            continue
        newL = [lis[q][0]]
        for xx in lis[q]:
            for yy in newL:
                if yy[0] - xx[0] >= 0 and yy[1] - xx[1] >= 0:
                    continue
                newL.append(xx)
        lis[q] = newL
    if len(lis[cnt]) != 0:
        cnt += 1
        lis[cnt] = []
        if cnt >= 54:
            pprint(lis)

print(ans if swi else -1)
