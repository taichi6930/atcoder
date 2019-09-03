n, k = map(int, input().split())
a = list(map(int, input().split()))
aSum = 0
for i in range(k):
    aSum += sum(a[i: n - i])
print(aSum)
