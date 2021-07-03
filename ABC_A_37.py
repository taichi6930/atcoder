import math

a, b, c = map(int, input().split())
print(math.floor(c/min(a, b)))
