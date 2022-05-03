from collections import Counter
from math import gcd
n, k = map(int, input().split())
XY = sorted([list(map(int, input().split())) for _ in range(n)])
xyList = []

for i in range(n - 1):
    for j in range(i + 1, n):
        st = ''
        dx = XY[j][0] - XY[i][0]
        dy = XY[j][1] - XY[i][1]
        x, y = XY[j][0], XY[j][1]

        # dxが0の時、ただの縦直線なので、"dx,dy,{x座標}"を追加する
        if dx == 0:
            st += 'x=' + str(x)
            xyList.append(st)
            continue

        # dyが0の時、ただの横直線なので、"dx,dy,{y座標}"を追加する
        if dy == 0:
            st += 'y=' + str(y)
            xyList.append(st)
            continue

        # dx、dyの最適化を行う
        st += "dx=" + str(dx) + ',' + "dy=" + str(dy) + ','
        dx, dy = dx // gcd(dx, dy), dy // gcd(dx, dy)

        # y = ax + b = (dy / dx)x + b より
        # b = y - (dy / dx)x
        # b = bt / bb とすると
        # 分子bt = y * dx - x * dy
        # 分子bb = dx とする
        bt = y * dx - x * dy
        bb = dx

        # dt、dbの最適化を行う
        bt, bb = bt // gcd(bt, bb), bb // gcd(bt, bb)

        st += 'bt=' + str(bt) + ',' + 'bb=' + str(bb)
        xyList.append(st)
print(Counter(xyList))
