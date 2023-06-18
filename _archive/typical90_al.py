import math

a, b = map(int, input().split())
ans = max(a, b) // math.gcd(a, b) * min(a, b)
print("Large" if ans > 10 ** 18 else ans)
