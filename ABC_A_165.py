import math

k = int(input())
a,b = map(int, input().split())
print(math.floor(k/b) * b)