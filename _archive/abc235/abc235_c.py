from collections import *
n, q = map(int, input().split())
A = list(map(int, input().split()))
dic = {}
cnt = {}

for i, a in enumerate(A):
    if not a in dic:
        dic[a] = deque()
        cnt[a] = 0
    dic[a].append(i + 1)
    cnt[a] += 1

for _ in range(q):
    x, k = map(int, input().split())
    if x not in dic.keys():
        print(-1)
        continue
    if cnt[x] < k:
        print(-1)
        continue
    print(dic[x][k - 1])
