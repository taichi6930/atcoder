from math import ceil
from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
A = [-1 * a for a in list(map(int, input().split()))]
heapify(A)

for _ in range(m):
    heappush(A, ceil(heappop(A) / 2))

print(-1 * sum(A))
