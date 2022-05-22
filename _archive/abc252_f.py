from collections import *
from heapq import *
n, l = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
A = A + ([] if l - sum(A) == 0 else [l - sum(A)])
heapify(A)

for i in range(len(A) - 1):
    k1 = heappop(A)
    k2 = heappop(A)
    k = k1 + k2
    ans += k
    heappush(A, k)
print(ans)
