n, m, k, s, t, x = map(int, input().split())  # 始点がs, 終点がt
UV = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    UV[v - 1].append(u - 1)
    UV[u - 1].append(v - 1)

ans = 0


def dfs(now_position, count, x_swi):
    global t, k, ans, x
    if count == k:
        if x_swi and now_position == t - 1:
            print(ans)
            ans += 1
        return
    count += 1

    for w in UV[now_position]:
        if w == x:
            dfs(w, count, not(x_swi))
            continue
        dfs(w, count, x_swi)


dfs(s - 1, 0, True)

print(ans)
