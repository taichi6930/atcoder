from collections import deque

n = int(input())
S = deque(list(input()))
sNum = n
ss = deque()
ssNum = 0
cnt = 1

for i in range(10 ** 9):
    if sNum <= 2:
        break
    if S[0] + S[1] + S[2] == 'ARC':
        for _ in range(3):
            S.popleft()
        sNum -= 3
        if cnt % 2 == 1:
            S.appendleft('R')
            sNum += 1
            if ssNum > 0:
                k = ss.pop()
                S.appendleft(k)
                ssNum -= 1
                sNum += 1
        else:
            S.appendleft('C')
            S.appendleft('A')
            sNum += 2
        cnt += 1
    else:
        k = S.popleft()
        ss.append(k)
        sNum -= 1
        ssNum += 1

print(cnt - 1)
