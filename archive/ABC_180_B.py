import math

n = int(input())
X = list(map(int, input().split()))
m, u2, c = 0, 0, 0
for x in X:
    x = abs(x)
    m += x
    u2 += x**2
    c = max(c, x)
print(m)
print(math.sqrt(u2))
print(c)
