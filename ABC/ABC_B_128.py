n = int(input())
sList, pList = [], []
for i in range(n):
    s, p = map(str, input().split())
    sList.append(s)
    pList.append(p)

sListSet = sorted(set(sList))
pListSet = sorted(set(pList), reverse=True)

spList = []
for i in range(n):
    spList.append(sListSet.index(sList[i]) * 1000 + pListSet.index(pList[i]))

for i in range(n):
    print(spList.index(sorted(spList)[i]) + 1)
