n, m = map(int, input().split())
listA = []
listB = []
ans = "IMPOSSIBLE"
for i in range(m):
    a, b = map(int, input().split())
    maxAB = max(a, b)
    minAB = min(a, b)
    if minAB == 1 or maxAB == n:
        if minAB == 1:
            listA.append(maxAB)
            if listB.count(maxAB) == 1:
                ans = "POSSIBLE"
                break
        if maxAB == n:
            listB.append(minAB)
            if listA.count(minAB) == 1:
                ans = "POSSIBLE"
                break
print(ans)
