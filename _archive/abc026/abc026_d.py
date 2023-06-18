
from math import *


def f(t):
    global a, b, c
    return a * t + b * sin(c * t * pi)


a, b, c = map(int, input().split())
cn = 0
cn2 = 10 ** 9

for i in range(10):
    for j in range(cn, cn2):
        if f(j * 10 ** (-1 * i)) >= 100:
            cn2 = j * 10 ** (-1 * i) + 1
            cn1 = cn2 - j * 10 ** (-1 * i - 1)
            break

print(cn)
