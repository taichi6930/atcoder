import pprint
h, w = map(int, input().split())
hw = [[0 for _ in range(w)] for _ in range(h)]
Q = int(input())
ra, ca, rb, cb = 0, 0, 0, 0
ans = False


def dfs(r, c, rb, cb, arr):
    global hw, ans, h, w
    if ans:
        return
    if r < 0 or c < 0 or w - 1 < r or h - 1 < c:
        return
    if hw[r][c] == 0:
        return
    if r == rb and c == cb:
        ans = True
        return
    rc = str(r) + '-' + str(c)
    if rc in arr:
        return
    arr.append(rc)

    for z in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        dfs(r + z[0], c + z[1], rb, cb, arr)


for p in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r, c, = q[1] - 1, q[2] - 1
        hw[r][c] = 1
        continue
    if q[0] == 2:
        ans = False
        ra, ca, rb, cb = q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1
        dfs(ra, ca, rb, cb, [])
        print('YNeos'[not(ans)::2])
        continue
