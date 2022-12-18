from collections import *
n = int(input())
A = sorted(list(map(int, input().split())))
AA = [A[:n // 2], A[n // 2:]]
swi = (n + 1) % 2
x, y = 0, 0
XY = []

for i in range(n):
    swi = (swi + 1) % 2
    k = AA[swi].pop()
    if x == 0 and y == 0:
        x = k
        y = x - y
        continue
    x = k
    XY.append([x, y])
    y = x - y

print(y)
for xy in XY:
    print(*xy)
