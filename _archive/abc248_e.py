from math import gcd
from collections import Counter
n, k = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(n)]
tateCounter = Counter()
abCounter = Counter()

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

for q in list(tateCounter.values()):
    ans += q * (q - 1) // 2

for q in list(abCounter.values()):
    ans += q * (q - 1) // 2

print(ans)
