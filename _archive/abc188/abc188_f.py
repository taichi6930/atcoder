x, y = map(int, input().split())
cnt = 0
lis = [[abs(y - x), x]]

if x == y:
    print(0)
    exit()

for cnt in range(10 ** 19):
    newLis = []
    setLis = set()
    for j in range(len(lis)):
        li = lis[j][1]
        if not li * 2 in setLis:
            newLis.append([abs(y - li * 2), li * 2])
            setLis.add(li * 2)
        if not li + 1 in setLis:
            newLis.append([abs(y - (li + 1)), li + 1])
            setLis.add(li + 1)
        if not li - 1 in setLis:
            newLis.append([abs(y - (li - 1)), li - 1])
            setLis.add(li - 1)
    lis = sorted(newLis)
    if lis[0][0] == 0:
        print(cnt + 1)
        break
# print(lis, cnt)
