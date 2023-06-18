import math
n = int(input())
k = math.ceil((-1 + (1 + 8 * n) ** 0.5) / 2)
j = k * (k + 1) // 2 - n
for i in range(1, k + 1):
    if j == i:
        continue
    print(i)
