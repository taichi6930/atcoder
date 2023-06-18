from functools import reduce
from operator import mul


mod = 10 ** 9 + 7


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    S = int(input())
    ans = 0

    for i in range(1, 10000):
        # i: 箱の数

        # d: 敷居の数
        d = i - 1
        e = S - i * 3

        if e < 0:
            break

        ans = (ans + cmb(e + d, d)) % mod
    print(ans % mod)


if __name__ == '__main__':
    main()
