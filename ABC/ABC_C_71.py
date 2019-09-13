n = int(input())
a = list(map(int, input().split()))
aSet = sorted(set(a), reverse=True)
print(a, aSet)
recStock = 0
recSquare = 0
for i in aSet:
    aCnt = a.count(i)
    if aCnt >= 4:
        rectangle = i * 2
        break
    elif aCnt >= 2:
        if recStock > 0:
            recSquare = i * recStock
        else:
            recStock = i
print(recSquare)
