n = int(input())
a = list(map(int, input().split()))
aSum = sum(a)
aLen = len(a)
aCnt = 0
st = 0
if aSum % aLen != 0:
    print(-1)
else:
    for i in range(n):
        if sum(a[st:i+1])/len(a[st:i+1]) == aSum / aLen:
            aCnt += i - st
            st = i + 1
    print(aCnt)
