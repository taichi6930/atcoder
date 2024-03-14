def main():
    n = int(input())
    A = list(map(int, input().split()))
    sumA = sum(A)
    dp = [[[10000000 for _ in range(sumA + 1)]
           for _ in range(sumA + 1)]
          for _ in range(n)]

    dp[0][0][0] = 0

    for i in range(n - 1):
        for j in range(sumA + 1):
            for k in range(j + 1):
                for l in range(sumA - j + 1):
                    d = ((k - l) ** 2 + 1) ** 0.5
                    dp[i + 1][j + l][l] = min(
                        dp[i + 1][j + l][l], dp[i][j][k] + d)
    print(dp[-1][sumA][0])


if __name__ == '__main__':
    main()
