from math import *
h, n = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
abest, bbest = 0, 0
ans = 10 ** 10

for i, (a, b) in enumerate(AB):
    if b * abest > a * bbest:
        continue
    abest, bbest = a, b

for i, (a, b) in enumerate(AB):
    ans = min(ans, b + bbest * int(ceil((h - a) / abest)))

print(ans)
