def main():
    n = int(input())
    A = list(map(int, input().split()))
    dp = [[0 for _ in range(21)]for _ in range(n - 1)]

    dp[0][A[0]] = 1
    for i in range(1, n - 1):
        a = A[i]
        for j in range(21):
            if j + a < 21 and j + a >= 0:
                dp[i][j + a] += dp[i - 1][j]
            if j - a < 21 and j - a >= 0:
                dp[i][j - a] += dp[i - 1][j]
    print(dp[-1][A[-1]])


if __name__ == '__main__':
    main()
