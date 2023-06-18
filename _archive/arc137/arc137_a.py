import math
l, r = map(int, input().split())

y = r

ans = 0

for _ in range(r + 1):
    if math.gcd(l, y) == 1:
        ans = y - l
        break
    y -= 1

for x in range(l, l + ans + 1):
    if r - x < ans:
        break
    for i in range(r - y + 1):
        yy = r - i
        if math.gcd(x, yy) == 1:
            ans = max(ans, yy - x)
            break

print(ans)
