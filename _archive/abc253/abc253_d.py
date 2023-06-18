from math import *
n, a, b = map(int, input().split())
a, b = min(a, b), max(a, b)


def sum_arithmetic_progression(tolerance, num):
    return(num * (num + 1) // 2) * tolerance


aNum = n // a
bNum = n // b
lcm = (a * b // gcd(a, b))
abNum = n // lcm

print(
    sum_arithmetic_progression(1, n)
    - sum_arithmetic_progression(a, aNum)
    - sum_arithmetic_progression(b, bNum)
    + sum_arithmetic_progression(lcm, abNum)
)
