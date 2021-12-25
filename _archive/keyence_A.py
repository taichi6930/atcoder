import math


def main():
    [h, w, n] = [int(input()) for _ in range(3)]
    print(math.ceil(n/max(h, w)))


if __name__ == '__main__':
    main()
