n = int(input())
aList = list(map(int, input().split()))
aLen = len(aList)
aSet = sorted(list(set(aList)))
aSum = 0
for a in aSet:
    aCount = aList.count(a)
    if aCount > a:
        aSum += aCount - a
    if aCount < a:
        aSum += aCount
    aLen -= aCount
    if a > aLen:
        aSum += aLen
        break

print(aSum)
