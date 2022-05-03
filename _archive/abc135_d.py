from pprint import pprint
S = list(input())[::-1]
modList = [i for i in range(10)]
dp = [[0 for _ in range(13)] for _ in range(len(S))]
if S[0] == '?':
    for i in range(10):
        dp[0][i] = 1
else:
    dp[0][int(S[0])] = 1

for i in range(1, len(S)):
    s = S[i]
    Q = [modList[int(s)]] if s != '?' else modList
    print(Q)
    for q in Q:
        for j in range(len(S)):
            dp[i][(j + q) % 13] += dp[i - 1][j]
    for k in range(10):
        modList[k] = (modList[k] * 10) % 13

pprint(dp)
