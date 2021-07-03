h, w = map(int, input().split())
aList = [None] * h
hSum = [0] * h
wSum = [0] * w

for i in range(h):
    a = list(map(int, input().split()))
    aList[i] = a
    hSum[i] = sum(a)
    for j in range(w):
        wSum[j] += a[j]

for i in range(h):
    ans = ""
    for j in range(w):
        ans += str(-aList[i][j] + hSum[i] + wSum[j]) + " "
    print(ans)
