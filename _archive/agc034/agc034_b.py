from collections import *
beforeS = deque()
afterS = deque(list(input().replace('BC', 'D')))
cntBeforeS = 0
cntAfterS = len(afterS)
cnt = 0

for i in range(10 ** 9):
    if cntAfterS <= 1:
        break

    s1 = afterS.popleft()
    s2 = afterS.popleft()

    if s1 != 'A' or s2 != 'D':
        cntBeforeS += 1
        cntAfterS -= 1
        beforeS.append(s1)
        afterS.appendleft(s2)
        continue

    cnt += 1
    afterS.appendleft(s1)
    afterS.appendleft(s2)

    if cntBeforeS > 0:
        if beforeS[-1] != 'A':
            continue
        cntBeforeS -= 1
        cntAfterS += 1
        afterS.appendleft(beforeS.pop())

print(cnt)
