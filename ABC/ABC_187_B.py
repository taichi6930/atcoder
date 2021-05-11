n = int(input())
num = 0
xyList = [None] * n

for i in range(n):
    xyList[i] = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        a = (xyList[i][1] - xyList[j][1]) / (xyList[i][0] - xyList[j][0])
        if a >= -1 and a <= 1:
            num += 1

print(num)
