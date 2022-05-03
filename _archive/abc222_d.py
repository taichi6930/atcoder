n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0 for _ in range(max(B) + 1)] for _ in range(n)]
for i in range(A[0], B[0] + 1):
    dp[0][i] += 1

for i in range(n - 1):
    for j in range(A[i], B[i] + 1):
        for k in range(max(A[i + 1], j), B[i + 1] + 1):
            dp[i + 1][k] = (dp[i + 1][k] + dp[i][j]) % 998244353

print(sum(dp[-1]) % 998244353)
