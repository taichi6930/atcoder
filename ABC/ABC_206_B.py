import math


def main():
    n = int(input())
    a = math.ceil((-1 + (1 + 8 * n) ** 0.5) / 2)
    print(a)


if __name__ == '__main__':
    main()
