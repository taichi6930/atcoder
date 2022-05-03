
from collections import Counter


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


n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

cA = Counter(A)
keyscA = sorted(cA.keys())
accCA = [0]

for keyCA in keyscA:
    accCA.append(accCA[-1] + cA[keyCA])

accCA = accCA[1:]
sumMax = 0

for keyCA in keyscA:

print(accCA)
