n = int(input())
P = list(map(int, input().split()))
minP = 0
pList = [True for _ in range(300000)]

for i, p in enumerate(P):
    pList[p] = False
    for j in range(300000):
        if pList[minP]:
            print(minP)
            break
        minP += 1
