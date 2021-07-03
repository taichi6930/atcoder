s = int(input())

x1, y1 = 0, 0
x2, y2 = 10 ** 9, 1
x3 = (x2 * 2 - s) % x2
y3 = (s + x3) // x2

print(x1, y1, x2, y2, x3, y3)
