n = int(input())
A = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n - 1)]
dp[0] = [n, n]

for i in range(max(n - 2, 0)):
    dp[i + 1][0] = dp[i][0] + dp[i][1]
    dp[i + 1][1] = dp[i][0]

ans = A
for i in range(n - 1):
    [plusNum, minusNum] = dp[i]
