n = int(input())
d, x = map(int, input().split())
aSum = n + x
for i in range(n):
    aSum += (d - 1) // int(input())
print(aSum)
