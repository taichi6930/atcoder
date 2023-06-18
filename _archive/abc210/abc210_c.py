# しゃくとり法
n, k = map(int, input().split())
C = list(map(int, input().split()))

ans = 0

cSet = set()
cDic = {i: 0 for i in C}

for z in range(k - 1):
    q = C[z]
    cSet.add(q)
    cDic[q] += 1

for s in range(n - k + 1):
    if s > 0:
        r = C[s - 1]
        cDic[r] = max(0, cDic[r] - 1)
        if cDic[r] == 0:
            cSet.discard(r)

    q = C[k - 1 + s]
    cSet.add(q)
    cDic[q] += 1
    ans = max(ans, len(cSet))

print(ans)
