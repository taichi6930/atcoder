def main():
    n, m = map(int, input().split())
    a, b = list(), list()
    ans = True

    for i in range(n):
        b = list(map(int, input().split()))
        # 横のチェック
        for j in range(1, m):
            if b[j] - b[j - 1] != 1:
                ans = not(ans)
                break

        # 縦のチェック
        for k in range(m):
            if len(a) == 0:
                break
            if b[k] - a[k] != 7:
                ans = not(ans)
                break

        a = b.copy()
        if not(ans):
            break
    print("NYoe s"[ans::2])


if __name__ == '__main__':
    main()
