S = list(input())

chokudai = list('chokudai')
T = []
for s in S:
    if s in chokudai:
        T.append(s)

S = T
lenS = len(S)

dp = [[0 for _ in range(lenS)] for _ in range(8)]

dp[0] = [1 if S[i] == 'c' else 0 for i in range(lenS)]

for i in range(7):
    for j in range(lenS - 1):
        if dp[i][j] > 0:
            for k in range(j + 1, lenS):
                if S[k] == chokudai[i + 1]:
                    dp[i + 1][k] = (dp[i + 1][k] + dp[i][j]) % (10 ** 9 + 7)

print(sum(dp[-1]) % (10 ** 9 + 7))
