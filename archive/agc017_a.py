import collections
from functools import reduce
from operator import mul


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


n, p = map(int, input().split())
A = list(map(int, input().split()))
B = [A[i] % 2 for i in range(n)]
C = collections.Counter(B)
ans = 0
for i in range(n):
    k = C[1] - i * 2 - p
    if k < 0:
        break
    ans += cmb(C[1], k)

ans *= 2 ** C[0]

print(ans)
