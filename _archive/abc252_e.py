# ダイクストラ法
from heapq import *

n, m = map(int, input().split())
G = [[] for i in range(n + 1)]

for i in range(1, m + 1):
    a, b, c = map(int, input().split())
    G[a].append((i, b, c))
    G[b].append((i, a, c))

D = [10 ** 18] * (n + 1)
D[1] = 0

q = [(0, '', 1)]
while q:
    c, i, a = heappop(q)
    if D[a] < c:
        continue
    print(i)
    for i, b, d in G[a]:
        if D[b] > c + d:
            D[b] = c + d
            heappush(q, (c + d, i, b))
