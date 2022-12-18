import sys
from copy import deepcopy
n, x, y = map(int, input().split())
UV = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    UV[u - 1].append(v)
    UV[v - 1].append(u)

se = set([x])

sys.setrecursionlimit(500000)


def t(k, lis):
    global UV, x, y, se
    for i in UV[k - 1]:
        if i in se:
            continue
        if y == i:
            exit(print(*(lis + [y])))
        newLis = deepcopy(lis)
        newLis.append(i)
        se.add(i)
        t(i, newLis)


t(x, [x])
