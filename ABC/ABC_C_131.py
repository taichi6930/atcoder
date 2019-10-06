import math
import fractions


def calc(x):
    aa = math.ceil(a/x)*x
    bb = math.floor(b/x)*x
    return int((bb - aa) // x + 1)


a, b, c, d = map(int, input().split())
cd = c * d / fractions.gcd(c, d)
# print(b - a + 1, calc(cd), calc(c), calc(d))
print(int(b - a + 1 + calc(cd) - calc(c) - calc(d)))
