from math import pi
from random import uniform
nIn = []

for i in range(1, 10 ** 12):
    nInAlpha = 0
    n = 10 ** 6
    for j in range(n):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            nInAlpha += 1

    if n % 1000000 == 0:
        print(n, nIn, 4 * nIn / n)
        break
