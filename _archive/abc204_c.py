# DFS, BFSの上限を増やす
from sys import *
setrecursionlimit(2000)

# 幅優先探索
n, m = map(int, input().split())
dic = {}
lis = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    lis[i - 1][i - 1] = 1

for _ in range(m):
    a, b = map(int, input().split())
    if not a - 1 in dic:
        dic[a - 1] = []
    dic[a - 1].append(b - 1)
    lis[a - 1][b - 1] = 1


def bfs(st, fi, oldSet):
    if not fi in dic:
        return
    for newfi in dic[fi]:
        if newfi in oldSet:
            continue
        if lis[st][newfi] == 1:
            continue
        lis[st][newfi] = 1
        oldSet.add(newfi)
        bfs(st, newfi, oldSet)


for st in list(dic.keys()):
    for fl in dic[st]:
        bfs(st, fl, set([st, fl]))

print(sum([sum(lis[i]) for i in range(n)]))
