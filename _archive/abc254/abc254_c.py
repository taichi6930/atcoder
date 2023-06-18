from math import *
from heapq import *
n, k = map(int, input().split())
A = list(map(int, input().split()))
sortA = sorted(A)

ADic = {i: [] for i in range(k)}
sortADic = {i: [] for i in range(k)}

for i in range(n):
    heappush(ADic[i % k], A[i])
    heappush(sortADic[i % k], sortA[i])

for i in range(k):
    for j in range(ceil((n - i) / k)):
        l = heappop(ADic[i])
        m = heappop(sortADic[i])
        if l != m:
            print('No')
            exit()

print('Yes')
