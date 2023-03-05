from collections import deque
n = int(input())
S = deque(list(input())[::-1])
T = deque(list(input())[::-1])
print(S, T)
num = 0
cnt = 0

for i in range(n ** n):
    print(S, T)
    if num == n:
        exit(print('Yes'))
    if T[0] == S[0]:
        cnt = 0
        num += 1
        S.popleft()
        T.popleft()
        continue
    t = T.popleft()
    T.append(t)
    cnt += 1
    if cnt >= n:
        print('No')
