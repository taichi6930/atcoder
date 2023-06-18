import math


def main():
    a, b, c, d = map(int,  input().split())
    taka = math.ceil(c / b)
    aoki = math.ceil(a / d)
    print('Yes' if taka <= aoki else 'No')


if __name__ == '__main__':
    main()
