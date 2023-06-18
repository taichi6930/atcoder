import math

a, b = map(int, input().split())
num = 0
for i in range(10**18):
    if a == b:
        exit(print(num))
    if a > b:
        c = math.ceil((a - b) / a)
        a -= b * c
        num += c
        continue
    if a < b:
        c = math.ceil((b - a) / b)
        b -= a * c
        num += c
        continue
