import math

a, b, c, d = map(int, input().split())
# print(b - a + 1)
e = c * d // math.gcd(c, d)
cMax = math.ceil(a / c)
cMin = math.floor(b / c)
# print(cMin - cMax + 1)
dMax = math.ceil(a / d)
dMin = math.floor(b / d)
# print(dMin - dMax + 1)
eMax = math.ceil(a / e)
eMin = math.floor(b / e)
# print(eMin - eMax + 1)

print(b - a + 1 + eMin - eMax + 1 - (cMin - cMax + 1) - (dMin - dMax + 1))
