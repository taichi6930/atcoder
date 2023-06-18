n, s, t = map(int, input().split())
cnt = 0
weightNow = 0

for i in range(n):
    weightNow += int(input())
    if (weightNow >= s) & (weightNow <= t):
        cnt += 1

print(cnt)
