# 文字の動的計画法
# S の i 文字目までを使って、chokudai の j 文字目まで選択する方法
S = input()

lenS = len(S)
mod = 10 ** 9 + 7
chokudai = list('chokudai')
lenChokudai = len(chokudai)

dp = [[0] * (lenChokudai + 1) for _ in range(lenS + 1)]

for i in range(lenS):
    dp[i][0] = 1

for i in range(lenS):
    for j in range(lenChokudai):
        if S[i] == chokudai[j]:
            dp[i + 1][j + 1] += dp[i + 1][j] + dp[i][j + 1]
        else:
            dp[i + 1][j + 1] += dp[i][j + 1]
        dp[i + 1][j + 1] %= mod

print(dp[lenS][-1])
