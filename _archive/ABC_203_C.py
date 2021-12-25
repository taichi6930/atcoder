n, k = map(int, input().split())
abList = [list(map(int, input().split())) for _ in range(n)]
abList.sort()
nowMoney = k
beforeA = 0
for i in range(n):
    [a, b] = abList[i]
    if nowMoney - (a - beforeA) < 0:
        beforeA += nowMoney
        nowMoney = 0
        break
    nowMoney += b - (a - beforeA)
    beforeA = a
print(beforeA + nowMoney)
