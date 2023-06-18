from collections import *
n = int(input())
M = []
mList = []
lis = defaultdict(list)

for _ in range(n):
    mLis = []
    m = int(input())
    for _ in range(m):
        p, e = map(int, input().split())

        mLis.append([p, e])

    M.append(m)
    mList.append(mLis)

print(M, mList, lis)
