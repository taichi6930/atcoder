n = int(input())
seatNum = n
for i in range(n):
    l, r = map(int, input().split())
    seatNum += r - l
print(seatNum)
