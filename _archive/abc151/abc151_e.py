n, k = map(int, input().split())
A = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7


def cmb(n, r, m=None):  # 組み合わせ計算
    from functools import reduce
    from operator import mul

    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    if m is None:
        return over // under
    return (over // under) % m


if k == 1:
    print(0)
    exit()

X = [1 for _ in range(n - k + 1)]

if k >= 2:
    for i in range(1, n - k + 1):
        X[i] = X[i - 1] * (k + i - 2) // i

q = 0
ans = 0
for i in range(n - k + 1):

    q += X[i]
    ans += q * (A[n - k + i - 1] - A[(n - 1) - (n - k + i - 1)])
    if ans < 0:
        continue
    ans %= mod

print(ans)
