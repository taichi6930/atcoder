MOD = 998244353


def solve(n, a, b):
    dp = [[0] * 2 for _ in range(n + 1)]  # dp[i][0/1] : i枚目を表/裏にした場合の数
    dp[1][0] = 1
    dp[1][1] = 1
    for i in range(2, n + 1):
        if a[i - 2] != b[i - 2]:
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = dp[i - 1][0]
        else:
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] = dp[i - 1][0]
        dp[i][0] %= MOD
        dp[i][1] %= MOD
    ans = (dp[n][0] + dp[n][1]) % MOD
    return ans


n = int(input())
a = []
b = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
print(solve(n, a, b))
