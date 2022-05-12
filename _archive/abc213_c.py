from bisect import bisect_left
h, w, n = map(int, input().split())
HWList = []
hSet = set()
wSet = set()
for i in range(n):
    a, b = map(int, input().split())
    hSet.add(a)
    wSet.add(b)
    HWList.append([a, b])

hList = sorted(list(hSet))
wList = sorted(list(wSet))

for i, [p, q] in enumerate(HWList):
    print(bisect_left(hList, p) + 1, bisect_left(wList, q) + 1)
