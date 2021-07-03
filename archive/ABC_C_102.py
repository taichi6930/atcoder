import math

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= i + 1

aAvg = math.floor(sum(a)/len(a))
aSum = 0
# print(sum(a)/len(a), aAvg, a)

for i in range(n):
    aSum += abs(a[i] - aAvg)
print(aSum)
