h, w = map(int, input().split())
aList = []
for i in range(h):
    a = input()
    if a.count(".") != w:
        aList.append(a)
h = len(aList)

aLen = w

print("---------")

for j in range(w):
    aSum = sum(aList[i][w - j - 1] == "." for i in range(h))
    if aSum == h:
        for a in range(h):
            aList[a] = aList[a][0:aLen-j-1] + aList[a][aLen-j:aLen]
        aLen -= 1


for i in range(h):
    print(aList[i])
