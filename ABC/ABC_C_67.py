n = int(input())
maxDiff = 10 ** 10
a = list(map(int, input().split()))
for i in range(n - 1):
    aDiff = abs(sum(a[0:i+1])-sum(a[i+1:n]))
    if aDiff < maxDiff:
        maxDiff = aDiff
        continue
print(maxDiff)
