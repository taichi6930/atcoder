from collections import Counter, deque
n = int(input())

stList2 = []
stList = []
for _ in range(n):
    s, t = map(str, input().split())
    stList.append([s, t])
    stList2 += [s, t]


cstList = Counter(stList2)

for i in range(n):
    swi = False
    for st in stList[i]:
        if cstList[st] == 1:
            swi = True
            break
        if cstList[st] == 2:
            if stList[i][0] == stList[i][1]:
                swi = True
                break
    if not(swi):
        print('No')
        exit()

print('Yes')
