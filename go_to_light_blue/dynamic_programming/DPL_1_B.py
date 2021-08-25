def main():
    N, max_w = map(int, input().split())
    vw = [None for _ in range(N)]
    for p in range(N):
        v, w = map(int, input().split())
        vw[p] = {'w': w, 'v': v}

    dp = [[0 for _ in range(max_w + 1)]] + \
        [[None for _ in range(max_w + 1)] for _ in range(N)]

    for n in range(N):
        for w in range(max_w + 1):
            dp[n + 1][w] = max(dp[n][w], dp[n][w - vw[n]['w']] +
                               vw[n]['v']) if w - vw[n]['w'] >= 0 else dp[n][w]

    print(dp[N][max_w])


if __name__ == '__main__':
    main()
