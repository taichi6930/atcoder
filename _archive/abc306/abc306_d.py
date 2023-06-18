n = int(input())
XY = [list(map(int, input().split())) for i in range(n)]
k = {0: 0, 1: 0}

for i, [x, y] in enumerate(XY):
    oldK = k.copy()
    if x == 0:
        k[0] = max(oldK[0], oldK[0] + y, oldK[1] + y)
    if x == 1:
        k[1] = max(oldK[0] + y, oldK[1])

print(max(k.values()))
