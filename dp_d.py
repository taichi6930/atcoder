n, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(W + 1)] for _ in range(n)]

for i, [w, v] in enumerate(WV):
    dp[i][w] = max(v, dp[i][w])
    if i == 0:
        continue
    for j in range(W + 1):
        k1 = dp[i - 1][j]
        k2 = 0

        if 0 <= j - w:
            k2 = dp[i - 1][j - w] + v
        dp[i][j] = max(k1, k2)


print(max(dp[-1]))
