from heapq import *
from collections import *
q = int(input())
querys = [list(map(int, input().split())) for _ in range(q)]

xList = Counter()
heapMinX = []
heapMaxX = []
heapify(heapMinX)
heapify(heapMaxX)
setX = set()

for query in querys:
    if query[0] == 3:
        minX = 0
        maxX = 0
        for i in range(10 ** 9):
            minXa = heappop(heapMinX)
            if minXa in setX:
                minX = minXa
                break
        for i in range(10 ** 9):
            maxXa = heappop(heapMaxX)
            if -1 * maxXa in setX:
                maxX = maxXa
                break
        print(-1 * maxX - minX)
        heappush(heapMinX, minX)
        heappush(heapMaxX, maxX)
        continue

    x = query[1]

    if query[0] == 1:
        if not x in setX:
            heappush(heapMinX, x)
            heappush(heapMaxX, -1 * x)
        setX.add(x)
        xList[x] += 1
        continue

    c = query[2]

    if query[0] == 2:
        xList[x] -= c
        if xList[x] <= 0:
            del xList[x]
            if x in setX:
                setX.remove(x)
        continue
