
import math


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


l = int(input())
if l == 12:
    print(1)
    exit()

print(comb(l - 1, 11))
