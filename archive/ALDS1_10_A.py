def main():
    n = int(input())
    dp = [1, 1] + [0 for _ in range(50)]
    for i in range(n - 1):
        dp[i + 2] = dp[i + 1] + dp[i]
    print(max(dp))


if __name__ == '__main__':
    main()
