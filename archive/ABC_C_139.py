n = int(input())
h = list(map(int, input().split()))
maxNum = 0
cntNum = 0

for i in range(n - 1):
    if h[i] >= h[i + 1]:
        cntNum += 1
    else:
        if cntNum > maxNum:
            maxNum = cntNum
        cntNum = 0

if cntNum > maxNum:
    maxNum = cntNum

print(maxNum)
