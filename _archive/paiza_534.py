from collections import deque
k = int(input())
MX = deque()
MX1, MX2 = deque(), deque()
msum = 0


for _ in range(k):
    m, x = map(int, input().split())
    msum += m
    MX.append([m, x])

cnt = msum // 2
swi = False
for i in range(k):
    [m, x] = MX[i]
    if swi:
        MX2.append([m, x])
        continue
    if cnt <= m:
        MX1.append([cnt, x])
        MX2.append([m - cnt, x])
        swi = True
        continue
    MX1.append([m, x])
    cnt -= m

ans = 0
cnt = msum // 2
for i in range(10 ** 10):
    if cnt == 0:
        break
    [m1, x1] = MX1[0]
    [m2, x2] = MX2[0]
    mMin = min(m1, m2)
    ans += abs(x1 - x2) * mMin
    cnt -= mMin
    if mMin == m1:
        MX1.popleft()
        MX2[0] = [m2 - m1, x2]
        continue
    if mMin == m2:
        MX2.popleft()
        MX1[0] = [m1 - m2, x1]
        continue

print(ans)
