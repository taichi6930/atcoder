import collections
import math

alphaList = list("abcdefghijklmnopqrstuvwxyz")


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    s = list(input())
    n = len(s)

    for i in range(n):
        c = collections.Counter(s)
        print(c)


if __name__ == '__main__':
    main()
