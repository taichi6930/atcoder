from math import *
n = int(input())

ans = 0

for a in range(n):
    p = int(min(n, (n + a ** 2) ** 0.5))
    q = ceil(max(1, (1 + a ** 2) ** 0.5))
    r = p - q + 1
    if r <= 0:
        break
    ans += r

print(ans)
