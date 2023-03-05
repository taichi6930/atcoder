from itertools import accumulate
from bisect import bisect_left

n, t = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)
accA = [0] + list(accumulate(A))

t %= sumA

for i, a in enumerate(accA):
    if a < t:
        continue
    print(i, t - accA[i - 1])
    break
