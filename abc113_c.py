from collections import *
n, m = map(int, input().split())

IPY = [list(map(int, input().split())) for _ in range(m)]
yDic = defaultdict(list)
yyDic = defaultdict(dict)

for i in range(m):
    yDic[IPY[i][0]].append(IPY[i][1])

for i, key in enumerate(list(yDic.keys())):
    yDicList = sorted(yDic[key])
    for j, yy in enumerate(yDicList):
        yyDic[key][yy] = j + 1

for [p, y] in IPY:
    print('{:06}'.format(p) + '{:06}'.format(yyDic[p][y]))
