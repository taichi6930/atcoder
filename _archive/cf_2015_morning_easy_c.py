from itertools import accumulate
n, k, m, r = map(int, input().split())
S = sorted([0] + [int(input()) for _ in range(n - 1)], reverse=True)
accS = list(accumulate(S))
kr = k * r

if n == 1:
    exit(print(r))

if k == 1:
    exit(print(r if accS[0] < r else 0))

if kr - accS[k - 1] <= 0:
    exit(print(0))
if kr - accS[k - 2] > m:
    exit(print(-1))
print(kr - accS[k - 2])
