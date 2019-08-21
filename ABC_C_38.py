n = int(input())
a = list(map(int, input().split()))

b = []

cnt = 0
sum = 0
allSum = 0

for i in range(n-1):
    if a[i + 1] - a[i] > 0:
        cnt += 1
        sum += cnt
    else:
        if cnt != 0:
            b.append(sum)
            allSum += sum
            cnt = 0
            sum = 0

b.append(sum)
allSum += sum
print(allSum + n)
