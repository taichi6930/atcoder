from pprint import pprint
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
C = [list(input()) for _ in range(r)]
xyList = [[0, 1], [1, 0], [-1, 0], [0, -1]]

RCList = [[[sx - 1, sy - 1]]]
lastNewRCList = []
# 幅優先探索
for i in range(r * c):
    newRCList = []
    for rcList in RCList:
        rc = rcList[-1]
        for xy in xyList:
            newX = xy[0] + rc[0]
            newY = xy[1] + rc[1]
            newXY = [newX, newY]
            if C[newY][newX] == "#":
                continue
            if newXY in rcList:
                continue
            if newXY in lastNewRCList:
                continue
            if newXY == [gx - 1, gy - 1]:
                print(i + 1)
                exit()
            lastNewRCList.append(newXY)
            newrcList = rcList + [newXY]
            newRCList.append(newrcList)
    RCList = newRCList
    print(i + 1, len(RCList))
