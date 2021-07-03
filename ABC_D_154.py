n, k = map(int, input().split())
pList = list(map(int, input().split()))
pKList = [(1 + p)/2 for p in pList]
pListMax = 0

for i in range(n-k+1):
    if i == 0:
        res = sum(pKList[i:i+k])
    else:
        res = res - pKList[i-1] + pKList[i+k-1]
    pListMax = max(pListMax, res)
print(pListMax)
