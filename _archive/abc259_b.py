from math import *
a, b, d = map(int, input().split())
theta = d * pi / 180
print(a * cos(theta) - b * sin(theta), a * sin(theta) + b * cos(theta))
