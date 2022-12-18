from bisect import bisect_left
from itertools import accumulate
n, q = map(int, input().split())
A = sorted(list(map(int, input().split())))
accA = [0] + list(accumulate(A))
X = [int(input()) for _ in range(q)]

for i, x in enumerate(X):
    l = bisect_left(A, x)
    print(
        abs((l - 0) * x - (accA[l] - accA[0])) +
        abs((n - l) * x - (accA[n] - accA[l]))
    )
