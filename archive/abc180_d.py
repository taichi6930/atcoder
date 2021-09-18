import math


def main():
    x, y, a, b = map(int, input().split())
    print(min(math.ceil(math.log(((y - 1) / x), a)), math.ceil((y - x - 1)/b)))


if __name__ == '__main__':
    main()
