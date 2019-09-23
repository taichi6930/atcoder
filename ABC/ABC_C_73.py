import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
aSum = 0
cnt = 0
for i in range(n):
    aCnt = a.count(a[cnt])
    if aCnt % 2 == 1:
        aSum += 1
    cnt += aCnt
    if cnt >= n:
        break


print(aSum)
