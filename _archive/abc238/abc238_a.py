import math


def main():
    n = int(input())
    print('Yes' if n > 2 * math.log(n, 2) else 'No')


if __name__ == '__main__':
    main()
