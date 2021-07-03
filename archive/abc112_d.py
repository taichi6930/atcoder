import collections
import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    n, m = map(int, input().split())
    maxGcd = math.floor(m / n)
    print(maxGcd)


if __name__ == '__main__':
    main()
