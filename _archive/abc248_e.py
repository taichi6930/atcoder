from math import gcd
from collections import Counter
n, k = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(n)]
tateCounter = Counter()
abCounter = Counter()


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
    print('Infinity')
    exit()

for i in range(n - 1):
    for j in range(i + 1, n):
        [x1, y1] = XY[i]
        [x2, y2] = XY[j]

        # x1 = x2 の場合、縦直線
        if x1 == x2:
            tateCounter[x1] += 1
            continue

        ab = abs(x2 - x1)
        at = y2 - y1 if x2 - x1 >= 0 else - (y2 - y1)
        ab, at = ab // gcd(ab, at), at // gcd(ab, at)

        ab_b = ab * y1 - at * x1
        if ab_b == 0:
            bt = 0
            bb = 1
        else:
            bt = (ab_b if ab > 0 else -1 * ab) // gcd(ab_b, ab)
            bb = abs(ab) // gcd(ab_b, ab)
        abCounter[str(at) + '_' + str(ab) + '_' + str(bt) + '_' + str(bb)] += 1


ans = 0

for k, q in enumerate(list(tateCounter.values()) + list(abCounter.values())):
    # ans += cmb(q, k * (k - 1) // 2)
    print(q, (1 + (1 + 8 * q) ** 0.5) / 2)

print(tateCounter)
print(abCounter)
# print(ans)
