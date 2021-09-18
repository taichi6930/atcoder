import math


def main():
    a, b, c = map(int, input().split())

    maxL = a + b + c
    minL = max(0, a - b - c)
    print((maxL + minL) * (maxL - minL) * math.pi)


if __name__ == '__main__':
    main()
