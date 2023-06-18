import math


def main():
    x, y = map(int, input().split())
    print(max(math.ceil((y - x)/10), 0))


if __name__ == '__main__':
    main()
