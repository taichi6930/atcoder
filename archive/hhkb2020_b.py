def main():
    ans = 0

    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    for h in range(H):
        for w in range(W):
            ans += 1 if S[h][w: min(W, w + 2)].count(".") == 2 else 0
            ans += 1 if [S[h][w], S[min(H - 1, h + 1)][w]
                         if h + 1 <= H - 1 else 0].count(".") == 2 else 0

    print(ans)


if __name__ == '__main__':
    main()
