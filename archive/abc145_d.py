mod = 10 ** 9 + 7


def main():
    xy = list(map(int, input().split()))
    x, y = max(xy), min(xy)
    # x + yが3の倍数でなければなし
    if (x + y) % 3 != 0:
        print(0)
        return
    s = (x + y) // 3
    d = x - y

    numX, numY = x - s, y - s
    if numX * numY < 0:
        print(0)
        return
    comb = 1
    # 後で見直し
    for i in range(numX):
        comb *= (numX + numY - i) % mod
        comb *= pow(numX - i, mod - 2, mod)
        comb %= mod
    print(comb)


if __name__ == '__main__':
    main()
