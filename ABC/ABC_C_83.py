import math

x, y = map(int, input().split())
print(math.floor(math.log2(y/x)) + 1)
