import collections
n, m, t = map(int, input().split())
A = list(map(int, input().split()))
xSet = set()
XY = collections.deque([])

for i in range(m):
    x, y = map(int, input().split())
    xSet.add(x)
    XY.append([x, y])

for i, a in enumerate(A):
    t -= a
    if t <= 0:
        exit(print('No'))
    if i + 2 in xSet:
        t += XY[0][1]
        XY.popleft()

print('Yes')
