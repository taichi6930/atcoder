import math


def main():
    r, g, b, n = map(int,  input().split())
    cnt = 0
    for rr in range(math.ceil(n / r)):
        print(n - rr * r)


if __name__ == '__main__':
    main()
