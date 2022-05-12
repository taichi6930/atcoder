a, b, c = map(int, input().split())

AList = [1]

for i in range(100):
    k = (AList[-1] * a) % 10
    if k in AList:
        break
    AList.append(k)

if len(AList) == 1:
    print(1)
    exit()

AList[0] = AList[-1]
AList = AList[:-1]

BList = [1]

for i in range(100):
    k = (BList[-1] * b) % 10
    if k in BList:
        break
    BList.append(k)

if len(BList) != 1:
    BList[0] = BList[-1]
    BList = BList[:-1]

print(AList, BList)
