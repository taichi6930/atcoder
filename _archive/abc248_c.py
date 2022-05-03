n, m, k = map(int, input().split())

dp = [[0 for _ in range(n)] for _ in range(k + 1)]

for i in range(n):
    if i == 0:
        for j in range(1, m + 1):
            if j > k:
                break
            dp[j][i] = 1
    else:
        for a in range(1, k + 1):
            for b in range(1, m + 1):
                if a + b > k:
                    break
                dp[a + b][i] += dp[a][i - 1]

mod = 998244353
ans = 0
for q in range(k + 1):
    ans = (ans + (dp[q][-1]) % mod) % mod

print(ans)
