n, t = map(int, input().split())
aList = [int(input()) for _ in range(n)]
sum = t

for i in range(n - 1):
    k = aList[i + 1] - aList[i]
    sum += (t if k > t else k)

print(sum)
