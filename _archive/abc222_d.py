from itertools import *
# 累積和 + DP
mod = 998244353
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
k = max(B) + 1
dp = [[0 for _ in range(k)] for _ in range(n)]

for i in range(k):
    dp[0][i] = 1 if A[0] <= i and i <= B[0] else 0


for j in range(1, n):
    accDp = list(accumulate(dp[j - 1]))

    a = A[j]
    b = B[j]

    for i in range(a, b + 1):
        dp[j][i] = accDp[i] % mod

print(sum(dp[-1]) % mod)
