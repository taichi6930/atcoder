from pprint import pprint
N, W = map(int, input().split())
dp = [[0 for _ in range(W + 1)] for _ in range(N)]

for i in range(N):
    w, v = map(int, input().split())
    dp[i][w] = v
    if i == 0:
        continue
    for j in range(1, W + 1):
        if dp[i - 1][j] == 0:
            continue
        if j + w > W:
            dp[i][j] = dp[i - 1][j]
            continue
        # dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)


pprint(dp)
