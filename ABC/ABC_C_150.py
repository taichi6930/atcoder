n = int(input())
p, q = [list(map(int, input().split())) for _ in range(2)]

cnt = 0

pList = p
qList = q

pNumList = []
qNumList = []

for i in range(n):
    pNumList.append(i+1)
    qNumList.append(i+1)

for i in range(n):
    p = pList
    q = qList
    if p[0] - q[0] > 0:
        cnt += (abs(p[0] - q[0]))**(n-1-i)
    else:
        cnt -= (abs(p[0] - q[0]))**(n-1-i)
    pNumList.pop(p[0]-1)
    qNumList.pop(q[0]-1)
    p = p[1:n-i]
    q = q[1:n-i]
    print(cnt, p, q, pNumList, qNumList)
    ppNumList = pNumList
    qqNumList = qNumList

    print(ppNumList[0], qqNumList[0])
    print(p.index(ppNumList[0]))
    pList = []
    qList = []
    for j in range(n-i-1):
        pList.append(p.index(ppNumList[j]) + 1)
        qq.append(q.index(qqNumList[j]) + 1)
        pNumList[j] = pNumList.index(ppNumList[j]) + 1
        qNumList[j] = qNumList.index(qqNumList[j]) + 1
    print(cnt, p, q, pNumList, qNumList)
    if len(p) == 1:
        break
    p = pp
    q = qq


print(abs(cnt))
