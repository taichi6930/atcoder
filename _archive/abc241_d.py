from bisect import bisect_left
q = int(input())
Query = [list(map(int, input().split())) for _ in range(q)]
setA = set()
dicA = {}

for p, query in enumerate(Query):
    c = query[0]
    if c == 1:
        x = query[1]
        if not x in setA:
            dicA[x] = 0
        setA.add(x)
        dicA[x] += 1
        continue
    [x, k] = query[1:3]

    a = -1 if c == 2 else 1
    cnt = 0
    listA = list(setA)

    if c == 2:
        ans = -1
        r = min(max(bisect_left(listA, x) - a, 0), len(setA) - 1)
        for i in range(10):
            if r < 0 or r >= len(listA):
                break
            if listA[r] > x:
                r -= 1
                continue
            cnt += dicA[listA[r]]
            if cnt >= k:
                ans = listA[r]
                break
            r -= 1

        print(ans)
        continue

    if c == 3:
        ans = -1
        r = min(max(bisect_left(listA, x) - a, 0), len(setA) - 1)
        for i in range(10):
            if r < 0 or r >= len(listA):
                break
            if listA[r] < x:
                r += 1
                continue
            cnt += dicA[listA[r]]
            if cnt >= k:
                ans = listA[r]
                break
            r += 1

        print(ans)
        continue
