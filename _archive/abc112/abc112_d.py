from math import gcd
n, m = map(int, input().split())
ans = 1

for i in range(1, 10 ** 9):
    if m // n - i + 1 <= ans:
        break
    ans = max(ans, gcd(m // n - i + 1,  m - (m // n - i + 1) * (n - 1)))

print(ans)
