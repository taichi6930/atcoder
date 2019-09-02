import math

a, b, x = map(int, input().split())
minNum = a // x
print(math.ceil((b - (minNum * x)) / x))
