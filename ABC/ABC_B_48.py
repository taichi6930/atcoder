import math

a, b, x = map(int, input().split())
minNum = math.ceil(a / x) * x
print(int(b - minNum + x - ((b - minNum + x) % x))//x if minNum <= b else 0)
