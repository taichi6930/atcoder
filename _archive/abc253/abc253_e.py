n, m, k = map(int, input().split())
dp = [[0 for _ in range(m + 1)] for _ in range(n)]
dp[0] = [i for i in range(m + 1)]
mod = 998244353

for i in range(1, n):
    for j in range(1, m + 1):
        dp[i][j] = dp[i][j - 1]
        dp[i][j] -= dp[i - 1][j] - dp[i - 1][j - 1] if k == 0 else 0
        dp[i][j] += (dp[i - 1][max(0, j - k)] - dp[i - 1][0]) % mod
        dp[i][j] %= mod
        dp[i][j] += (dp[i - 1][m] - dp[i - 1][min(j + k - 1, m)]) % mod
        dp[i][j] %= mod


print(dp[-1][-1])
