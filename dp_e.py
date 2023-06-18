n, W = map(int, input().split())
WV = []
sumV = 0
for _ in range(n):
    w, v = map(int, input().split())
    sumV += v
    WV.append([w, v])

dp = [[None for _ in range((sumV) + 1)] for _ in range(n)]

for i, [w, v] in enumerate(WV):
    if dp[i][v] is None:
        dp[i][v] = w
    else:
        dp[i][v] = min(w, dp[i][v])
    if i == 0:
        continue
    for j in range(sumV + 1):
        if dp[i][j] is None:
            dp[i][j] = dp[i - 1][j]
        elif dp[i - 1][j] is None:
            dp[i][j] = dp[i][j]
        else:
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
        k1 = dp[i][j]
        k2 = None
        if 0 <= j - v:
            if not dp[i - 1][j - v] is None:
                k2 = dp[i - 1][j - v] + w
        if k1 is None and k2 is None:
            dp[i][j] = None
            continue
        elif k2 is None:
            dp[i][j] = k1
            continue
        elif k1 is None:
            dp[i][j] = k2
            continue
        dp[i][j] = min(k1, k2)

ans = 0
for a, b in enumerate(dp[-1]):
    if b is None:
        continue
    if b <= W:
        ans = a

print(ans)
