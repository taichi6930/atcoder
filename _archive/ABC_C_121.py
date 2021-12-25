n, m = map(int, input().split())
abList = [list(map(int, input().split())) for _ in range(n)]
abList.sort()
abSum = 0
abNum = m
for ab in abList:
    a, b = ab[0], ab[1]
    if b < abNum:
        abSum += b * a
        abNum -= b
    else:
        abSum += abNum * a
        break
print(abSum)
