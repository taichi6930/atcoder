from math import *
n = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())
xa, ya = (x0 + xn2) / 2, (y0 + yn2) / 2

x1 = cos(2 * pi / n) * (x0 - xa) - sin(2 * pi / n) * (y0 - ya) + xa
y1 = sin(2 * pi / n) * (x0 - xa) + cos(2 * pi / n) * (y0 - ya) + ya

print(x1, y1)
