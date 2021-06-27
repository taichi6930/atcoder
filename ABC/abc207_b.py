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
    a, b, c, d = map(int, input().split())
    if c * d != b:
        n = a / (c * d - b)
        print(max(-1, math.ceil(n)))
        return
    print(-1)


if __name__ == '__main__':
    main()
