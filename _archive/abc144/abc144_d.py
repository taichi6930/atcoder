import math
a, b, x = map(int, input().split())

if a ** 2 * b >= 2 * x:
    # 三角形
    print(math.degrees(math.atan(x / a / b)))
else:
    print(math.degrees(math.atan(a / (b - (x / a * 2) / a))))
