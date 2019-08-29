n = int(input())
aList = []
for i in range(n):
    aList.append(list(input()))

bList = aList

for i in range(n):
    for j in range(n):
        bList[j][n - 1 - i - j] = aList[i][j]

for i in range(n):
    print(bList[i])
