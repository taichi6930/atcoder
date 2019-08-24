n = int(input())
a, b = map(int, input().split())
k = int(input())
pList = list(map(int, input().split()))
pList.append(a)
pList.append(b)
print(len(pList), len(set(pList)))

for i in range(len(pList)):
    if pList[i:len(pList)].count(pList[i]) > 1:
        print("NO")
        break
    if i == len(pList)-1:
        print("YES")
