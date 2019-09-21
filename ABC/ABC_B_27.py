n = int(input())
a = list(map(int, input().split()))
aSum = sum(a)
aLen = len(a)
aAvg = aSum / aLen
aCnt = 0
st = 0
if aSum % aLen != 0:
    print(-1)
else:
    swi = 0
