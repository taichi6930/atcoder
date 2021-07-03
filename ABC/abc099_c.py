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
    n = int(input())
    cnt = n
    a9Max = int(math.log(n, 9))
    a6Max = int(math.log(n, 6))
    for i in range(n):
        pass

    print(a9Max, a6Max)


if __name__ == '__main__':
    main()
