n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

aSet = set()
aDic = {i: 0 for i in A}

for s in range(n):
    if s > 0:
        r = A[s - 1]
        aDic[r] = max(0, aDic[r] - 1)
        if aDic[r] == 0:
            aSet.discard(r)

    for i in range(n):
        if s + ans >= n:
            break
        q = A[s + ans]
        aSet.add(q)
        aDic[q] += 1
        if len(aSet) > k:
            break
        ans += 1

print(ans)
