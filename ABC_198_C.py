import math
r, x, y = map(int, input().split())

a = (x ** 2 + y ** 2) ** 0.5
print(2 if a < r else int(math.ceil(a / r)))
