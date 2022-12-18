# BFS
n, m = map(int, input().split())
G = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

q = [0]
dist = [None for _ in range(n)]
cnt = [0 for _ in range(n)]
dist[0] = 0
cnt[0] = 1

for v in q:
    for vv in G[v]:
        if dist[vv] is None:
            dist[vv] = dist[v]+1
            q.append(vv)
            cnt[vv] = cnt[v]
        elif dist[vv] == dist[v]+1:
            cnt[vv] += cnt[v]
            cnt[vv] %= 10 ** 9 + 7

print(cnt[n - 1])
