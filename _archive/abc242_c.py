from pprint import pprint
n = int(input())

dp = [[1] + [0 for _ in range(n - 1)] for i in range(10)]

for i in range(1, n):
    for j in range(1, 10):
        dp[j][i] += dp[j][i - 1]
        if j - 1 > 0:
            dp[j][i] += dp[j - 1][i - 1]
        if j + 1 < 10:
            dp[j][i] += dp[j + 1][i - 1]
        dp[j][i] = dp[j][i] % 998244353
ans = sum([dp[j][-1] for j in range(1, 10)])
print(ans % 998244353)
