n, K = map(int, input().split())

# [食塩水の重量、食塩の濃度パーセント]
WP = [list(map(int, input().split())) for _ in range(n)]

# # [食塩水の重量、食塩の重量]
# dp = [[[0, 0] for _ in range(n)] for i in range(K)]

# dp[0][0] = [WP[0][0], WP[0][1] * WP[0][0] / 100]
# for i in range(1, n):
#     [a1, a2] = dp[0][i - 1]
#     [b1, b2] = [WP[i][0], WP[i][1] * WP[i][0] / 100]
#     dp[0][i] = [a1, a2] if a1 * b2 <= a2 * b1 else [b1, b2]

# for k in range(1, K):
#     dp[k][k] = [dp[k - 1][k - 1][0] + WP[k][0],
#                 dp[k - 1][k - 1][1] + WP[k][1] * WP[k][0] / 100]
#     for j in range(k + 1, n):
#         [a1, a2] = dp[k - 1][j - 1]
#         [b1, b2] = [dp[k - 1][j - 1][0] + WP[j][0],
#                     dp[k - 1][j - 1][1] + WP[j][1] * WP[j][0] / 100]
#         dp[k][j] = [a1, a2] if a1 * b2 <= a2 * b1 else [b1, b2]

# print(dp)
