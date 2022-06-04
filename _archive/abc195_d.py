from bisect import *
from collections import *
n, m, q = map(int, input().split())
WV = sorted([list(map(int, input().split())) for _ in range(n)],
            key=lambda x: (x[1]),
            reverse=True)
X = list(map(int, input().split()))
querys = [list(map(int, input().split())) for _ in range(q)]

for (l, r) in querys:
    ans = 0
    cNewX = Counter(X[:l - 1] + X[r:])
    for (w, v) in WV:
        keys = sorted(list(cNewX.keys()))
        b = bisect_left(sorted(list(cNewX.keys())), w)
        if len(keys) <= b:
            continue
        if w > keys[b]:
            continue
        if not keys[b] in keys:
            continue
        ans += v
        cNewX[keys[b]] -= 1
        if cNewX[keys[b]] == 0:
            del cNewX[keys[b]]
    print(ans)
