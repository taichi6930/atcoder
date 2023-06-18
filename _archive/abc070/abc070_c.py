import math
n = int(input())
T = list(set([int(input()) for _ in range(n)]))
ans = 1
for t in T:
    ans = ans * t // math.gcd(ans, t)
print(ans)
