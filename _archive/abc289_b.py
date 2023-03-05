from collections import deque
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = deque()
cnt = 0
ANS = []

for i in range(n + 1):
    if i == n:
        for _ in range(cnt):
            ANS.append(str(B.pop()))
        break
    if i + 1 in A:
        B.append(i + 1)
        cnt += 1
        continue
    ANS.append(str(i + 1))
    for _ in range(cnt):
        ANS.append(str(B.pop()))
    cnt = 0

print(' '.join(ANS))
