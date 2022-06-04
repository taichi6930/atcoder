# DFS, BFSの上限を増やす
from sys import *
setrecursionlimit(10000)

# 幅優先探索
n, m = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(m)]

dic = {}

for _, (x, y) in enumerate(XY):
    if not x - 1 in dic:
        dic[x - 1] = []
    dic[x - 1].append(y - 1)

print(dic)


def bfs(st, fi, oldSet):
    if not fi in dic:
        return
    for newfi in dic[fi]:
        if newfi in oldSet:
            continue
        # if lis[st][newfi] == 1:
        #     continue
        # lis[st][newfi] = 1
        oldSet.add(newfi)
        bfs(st, newfi, oldSet)


for st in list(dic.keys()):
    for fl in dic[st]:
        bfs(st, fl, set([st, fl]))

# print(sum([sum(lis[i]) for i in range(n)]))
