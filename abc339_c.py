n = int(input())
A = list(map(int, input().split()))

cnt = 0
for a in A:
    cnt = max(0, cnt + a)
print(cnt)
