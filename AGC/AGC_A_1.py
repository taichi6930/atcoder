n = int(input())
l = list(map(int, input().split()))
l = sorted(l)
lSum = 0
for i in range(n):
    lSum += min(l[2 * i], l[2 * i + 1])
print(lSum)
