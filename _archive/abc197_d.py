from math import sin, cos, pi
n = int(input())
x0, y0 = map(int, input().split())
xnp2, ynp2 = map(int, input().split())

xa, ya = (x0 + xnp2) / 2, (y0 + ynp2) / 2
sint = sin(2 * pi / n)
cost = cos(2 * pi / n)

print(xa, ya, sint, cost)
