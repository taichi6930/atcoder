import math


def main():
    a, b = map(int, input().split())

    print(math.floor(b / 4) - math.ceil(a / 4)
          - (math.floor(b / 100) - math.ceil(a / 100))
          + math.floor(b / 400) - math.ceil(a / 400) + 1)


if __name__ == '__main__':
    main()
