import math

t = int(input())
l, x, y = map(int, input().split())
q = int(input())

for i in range(q):
    e = int(input())
    h = l * (math.sin(math.pi * (-1 / 2) + 2 * math.pi * e / t) * 0.5 + 0.5)
    yc = l * (math.sin(math.pi * (-2 / 2) + 2 * math.pi * e / t) * 0.5)
    m = ((y - yc) ** 2 + (x) ** 2) ** 0.5
    print(math.degrees(math.atan2(h, m)))
