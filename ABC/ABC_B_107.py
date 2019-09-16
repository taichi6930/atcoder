h, w = map(int, input().split())
aList = []
for i in range(h):
    a = input()
    if a.count(".") != w:
        aList.append(a)
aLen = len(aList)
print(aList, aLen)

for j in range(w):
    aSum = 0
    for i in range(aLen):
        if aList[i][w-j-1] == ".":
            aSum += 1
    if aSum == aLen:
        for a in range(aLen):
            aList[a] = aList[a][0:aLen-j] + aList[a][aLen-j+1:aLen + 1]
        aLen -= 1


for i in range(aLen+1):
    print(aList[i])
