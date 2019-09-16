n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    minNum, minCnt = 0, -1
    for j in range(m):
        abcdLen = abs(ab[i][0]-cd[j][0]) + abs(ab[i][1]-cd[j][1])
        if minCnt == -1 or minCnt > abcdLen:
            minCnt, minNum = abcdLen, j + 1
    print(minNum)
