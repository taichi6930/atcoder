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
    primeList = collections.deque()
    for i in range(55555):
        if is_prime(i + 1):
            primeList.append(i + 1)

    n = int(input())


if __name__ == '__main__':
    main()
