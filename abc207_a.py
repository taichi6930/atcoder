import collections
import math

mod = 10 ** 9 + 7
alphaList = list("abcdefghijklmnopqrstuvwxyz")


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    a, b, c = map(int, input().split())
    print(a + b + c - min(a, b, c))


if __name__ == '__main__':
    main()
