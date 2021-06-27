from functools import reduce
from operator import mul


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
print(A)
