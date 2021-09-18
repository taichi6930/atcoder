def main():
    n = int(input())
    ans = 10 ** 9

    for a9 in range(10 ** 7):
        if a9 * 9 > n:
            break

        for a6 in range(10 ** 7):
            a1 = n - a9 * 9 - a6 * 6
            if a1 < 0:
                break
            if a1 > ans:
                continue

            a9num = 0 + a9
            a6num = 0 + a6
            cnt = a1

            for i in range(10 ** 9):
                cnt += a9num % 9
                a9num -= a9num % 9
                if a9num == 0:
                    break
                a9num = a9num // 9

            for j in range(10 ** 9):
                cnt += a6num % 6
                a6num -= a6num % 6
                if a6num == 0:
                    break
                a6num = a6num // 6

            ans = min(ans, cnt)

    print(ans)


if __name__ == '__main__':
    main()
