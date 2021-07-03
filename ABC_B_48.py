import math

a, b, x = map(int, input().split())
minNum = a // x
maxNum = b // x
print((maxNum - minNum) if a % x != 0 else b//x-a//x+1)
