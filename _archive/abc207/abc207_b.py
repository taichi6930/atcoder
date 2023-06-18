import math


def main():
    a, b, c, d = map(int, input().split())
    if c * d != b:
        n = a / (c * d - b)
        print(max(-1, math.ceil(n)))
        return
    print(-1)


if __name__ == '__main__':
    main()
