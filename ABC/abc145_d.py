from functools import reduce
from operator import mul


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return


if __name__ == '__main__':
    main()
