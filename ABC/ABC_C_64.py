aList = [0] * 8
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] >= 2800:
        aList[7] += 1
    else:
        aList[a[i]//400] += 1
aMin = 8 - aList.count(0)
aMax = aMin

if aList[7] > 1:
    aMax = 8
    if aList.count(0) > aList[7]:
        aMax = 7 - aList.count(0) + aList[7]
print(aMin, aMax)
