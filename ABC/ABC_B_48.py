import math

a, b, x = map(int, input().split())
minNum = math.ceil(a / x) * x
print(math.floor((b - minNum)/x) + 1 if minNum <= b else 0)
