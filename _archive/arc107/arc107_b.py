def main():
    n, k = map(int, input().split())
    ans = 0

    # 1 <= a,b,c,d <= n
    # (a + b) = k + (c + d)
    # ab = k + cd
    # 2<= ab,cd <= 2n
    # この条件を満たす組み合わせを決める
    # 2<= cd <= 2n - k

    arr = []

    for cd in range(2, min(2 * n + 1 - k, 2 * n + 1)):
        ab = k + cd
        if ab < 2 or 2 * n < ab:
            continue

        cnt = 1

        if ab <= n + 1:
            cnt *= ab - 1
        else:
            cnt *= 2 * n + 1 - ab

        if cd <= n + 1:
            cnt *= cd - 1
        else:
            cnt *= 2 * n + 1 - cd

        ans += cnt
    print(ans)


if __name__ == '__main__':
    main()
