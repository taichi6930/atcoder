import math
n = int(input())
rList = sorted([int(input()) for _ in range(n)], reverse=True)
sum = 0
for i in range(n):
    sum += rList[i] ** 2 * (-1) ** i

print(sum * math.pi)
