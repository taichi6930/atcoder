k = int(input())
mod = 10 ** 9 + 7


if k % 9 != 0:
    print(0)
    exit()
dp = [1] + [0] * k

for i in range(1, k + 1):
    for j in range(1, min(i, 9) + 1):
        dp[i] = (dp[i] + dp[i - j]) % mod

print(dp[-1] % mod)
