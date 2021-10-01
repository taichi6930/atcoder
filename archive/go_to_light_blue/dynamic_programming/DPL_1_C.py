def main():
    N, W = map(int, input().split())
    dp = [0 for _ in range(W + 1)]

    for i in range(1, N + 1):
        v, w = map(int, input().split())
        for j in range(w, W + 1):
            dp[j] = max(dp[j], dp[j - w] + v)
    print(max(dp))


if __name__ == '__main__':
    main()
