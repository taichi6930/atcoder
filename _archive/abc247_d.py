q = int(input())
sList = []
sListCnt = 0
cnt = 0
for _ in range(q):
    k = list(map(int, input().split()))
    if k[0] == 1:
        x, c = k[1], k[2]
        sList.append([x, c])
        sListCnt += 1
    if k[0] == 2:
        sumAns = 0
        c = k[1]
        for i in range(10 ** 9):
            if cnt > sListCnt:
                break
            [x1, c1] = sList[cnt]
            if c1 < c:
                sumAns += x1 * c1
                sList[cnt][1] = 0
                c -= c1
                cnt += 1
                continue
            if c1 >= c:
                sumAns += x1 * c
                sList[cnt][1] = sList[cnt][1] - c
                break
        print(sumAns)
