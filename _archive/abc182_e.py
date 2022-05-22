h, w, n, m = map(int, input().split())
ABList = [list(map(int, input().split())) for _ in range(n)]
CDList = [list(map(int, input().split())) for _ in range(m)]
lightList = [[0 for _ in range(w)] for _ in range(h)]
blockList = [[0 for _ in range(w)] for _ in range(h)]

for _, [c, d] in enumerate(CDList):
    blockList[c - 1][d - 1] = 1

for i, [a, b] in enumerate(ABList):
    lightList[a - 1][b - 1] = 1
    for j, [x, y] in enumerate([[1, 0], [0, 1], [-1, 0], [0, -1]]):
        for k in range(1, 10000):
            xx = a - 1 + k * x
            yy = b - 1 + k * y
            if not(0 <= yy < w and 0 <= xx < h):
                break
            if blockList[xx][yy] == 1:
                break
            lightList[xx][yy] = 1


print(sum([sum(l) for l in lightList]))
