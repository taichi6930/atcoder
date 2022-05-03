n = int(input())
A = list(map(int, input().split()))

mod = 998244353

dp = [[1 if i == A[0] else 0 for i in range(
    10)]] + [[0 for _ in range(10)] for _ in range(n - 1)]

for i in range(n - 1):
    for j in range(10):
        p = (A[i + 1] * j) % 10
        q = (A[i + 1] + j) % 10
        dp[i + 1][p] = (dp[i + 1][p] + dp[i][j]) % mod
        dp[i + 1][q] = (dp[i + 1][q] + dp[i][j]) % mod

for i in range(10):
    print(dp[-1][i])
