import math


def main():
    n, a, b = map(int,  input().split())
    x = list(map(int,  input().split()))
    sumX = 0
    for i in range(n-1):
        sumX += min(b, a * (x[i + 1] - x[i]))
    print(sumX)


if __name__ == '__main__':
    main()
