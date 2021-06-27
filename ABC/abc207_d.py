import math
import collections

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
    n = int(input())
    abList, cdList = [None] * n, [None] * n
    for ab in range(n):
        abList[ab] = map(int, input().split())

    for cd in range(n):
        cdList[cd] = map(int, input().split())


if __name__ == '__main__':
    main()
