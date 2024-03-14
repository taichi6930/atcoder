from pprint import pprint

S = list(input())[::-1]
dp = [[0 for i in range(13)] for _ in range(len(S))]
for i, s in enumerate(S):
    if s == "?":
        if i == 0:
            for k in range(10):
                dp[i][k] = 1
        else:
            for k in range(10):
                a = (int(k) * 10**i) % 13
                for j in range(13):
                    dp[i][j] = dp[i - 1][j - a]
        continue
    a = (int(s) * 10**i) % 13
    if i == 0:
        dp[i][a] = 1
        continue
    else:
        for j in range(13):
            dp[i][j] = dp[i - 1][j - a]
pprint(dp)
