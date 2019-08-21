n = int(input())
aList = list(map(int, input().split()))

rmSum = 0

for i in range(n):
    while True:
        if (aList[i] % 2 != 0) & (aList[i] % 3 != 2):
            break
        aList[i] -= 1
        rmSum += 1

print(rmSum)
