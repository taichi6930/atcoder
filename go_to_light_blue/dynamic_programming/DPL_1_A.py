def main():
    N, M = map(int, input().split())
    C = sorted(list(map(int, input().split())))
    dp = [i for i in range(N + 1)]

    for m in range(M):
        c = C[m]
        for n in range(c, N + 1):
            dp[n] = min(dp[n], dp[n - c] + 1)

    print(dp[-1])


if __name__ == '__main__':
    main()
