n = int(input())
a = list(map(int, input().split()))
aSet = sorted(set(a), reverse=True)
recStock = 0
recSquare = 0
for i in range(len(aSet)):
    aCnt = a.count(aSet[i])
    if aCnt >= 4:
        rectangle = aSet[i] * 2
        break
    elif aCnt >= 2:
        if recStock > 0:
            recSquare = aSet[i] * recStock
        else:
            recStock = aSet[i]
print(recSquare)
