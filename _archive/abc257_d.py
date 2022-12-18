from copy import deepcopy
from math import *
n = int(input())
XYP = [list(map(int, input().split())) for _ in range(n)]

xyList = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        xyList[i][j] = None if i == j else abs(XYP[i][0] - XYP[j][0]) + \
            abs(XYP[i][1] - XYP[j][1])

minS = [[10 ** 9 for _ in range(n)] for _ in range(n)]


def f(first, now, nowS, after):
    newAfter = deepcopy(after)
    newAfter.discard(now)

    for next in newAfter:
        nowS = max(nowS, ceil(xyList[now][next] / XYP[now][2]))
        minS[first][next] = min(nowS, minS[first][next])
        f(first, next, nowS, newAfter)


kSet = set([i for i in range(n)])

for i in range(n):
    f(i, i, 0, kSet)

print(minS)

