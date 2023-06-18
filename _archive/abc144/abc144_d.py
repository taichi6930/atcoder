import math
a, b, x = map(int, input().split())
print(math.degrees(math.atan(((2/a) * (b - x / a**2)
                              if x * 2 >= a ** 2 * b else (a * b ** 2)/(2 * x)))))
a, b, x = map(int, input().split())
if x * 2 >= a ** 2 * b:
    ans = (2/a) * (b - x / a**2)
else:
    ans = (a * b ** 2)/(2 * x)
print(math.degrees(math.atan(ans)))
