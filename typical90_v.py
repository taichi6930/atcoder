from math import *
a, b, c = map(int, input().split())
k = gcd(gcd(a, b), c)
print(a // k + b // k + c // k - 3)
