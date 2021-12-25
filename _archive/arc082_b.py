n = int(input())
P = list(map(int, input().split()))

cnt = 0

for i in range(n - 1):
    if P[i] == i + 1:
        cnt += 1
        P[i + 1], P[i] = P[i], P[i + 1]

if P[n - 1] == n:
    cnt += 1
print(cnt)
