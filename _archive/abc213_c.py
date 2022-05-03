from bisect import bisect_left
from collections import deque
h, w, n = map(int, input().split())
xyList = deque()
xset = set()
yset = set()

for _ in range(n):
    x, y = map(int, input().split())
    xyList.append([x, y])
    xset.add(x)
    yset.add(y)

for i, xy in enumerate(xyList):
    [x, y] = xy
    print(bisect_left(list(xset), x) + 1, bisect_left(list(yset), y) + 1)
