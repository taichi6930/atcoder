import math
mod = 10 ** 9 + 7


def main():
    n = int(input())
    print((10 ** n - 2 * 9 ** n + 8 ** n) % mod)


if __name__ == '__main__':
    main()
