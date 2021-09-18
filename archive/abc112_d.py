import math


def main():
    n, m = map(int, input().split())
    maxGcd = math.floor(m / n)
    print(maxGcd)


if __name__ == '__main__':
    main()
