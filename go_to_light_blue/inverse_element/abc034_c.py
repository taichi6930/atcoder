mod = 10 ** 9 + 7


def cmb(n, r, m=None):
    from functools import reduce
    from operator import mul

    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    if m is None:
        return over // under
    return (over // under) % m


def main():
    w, h = map(int, input().split())
    print(cmb((w - 1) + (h - 1), w-1, mod))


if __name__ == '__main__':
    main()
