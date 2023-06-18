from heapq import *
n = int(input())
ABheapq = {i + 1: [] for i in range(n)}
cnt = {i + 1: 0 for i in range(n)}
AB = [list(map(int, input().split())) for _ in range(n - 1)]
for i, [a, b] in enumerate(AB):
    ABheapq[a].append(b)
    ABheapq[b].append(a)
    cnt[a] += 1
    cnt[b] += 1

for i in range(n):
    heapify(ABheapq[i + 1])

print(ABheapq)

ansSet = set([1])

ans = [1]
now = 0

for i in range(10 ** 2):
    if cnt[ans[-1]] == 0:
        if ans[-1] == 1:
            break
        ans.append(ans[now])
        continue
    k = heappop(ABheapq[ans[-1]])
    cnt[ans[-1]] -= 1
    now = 0
    if k in ansSet:
        now -= 1
        continue
    ansSet.add(k)
    print(k, ABheapq)
    ans.append(k)

print(ans)
