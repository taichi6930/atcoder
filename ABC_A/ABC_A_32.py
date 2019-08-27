import math
a, b, n = [int(input()) for _ in range(3)]
c = a*b/math.gcd(a, b)
print(int(math.ceil(n/c) * c))
