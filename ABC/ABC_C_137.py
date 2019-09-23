n = int(input())
sListSum = 0
sList = [None] * n

for i in range(n):
    s = sorted(input())
    sListSum += sList.count(s)
    sList[i] = s

print(sListSum)
