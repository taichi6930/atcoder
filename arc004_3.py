def main():
    x, y = map(int, input().split('/'))
    print(x, y)
    ans = 0

    for n in range(1, 10 ** 9 + 1):
        und = 2 * y
        up = n * ((n + 1) * y - 2 * x)
        if up <= 0:
            continue
        if up % und != 0:
            continue
        if n * und // up < 1:
            break
        print(n, up // und, n * und // up)
        ans += 1

    if ans == 0:
        print('Impossible')


if __name__ == '__main__':
    main()
