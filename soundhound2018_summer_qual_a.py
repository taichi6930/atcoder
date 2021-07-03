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
    a, b = map(int, input().split())
    if a + b == 15:
        print("+")
        return
    if a * b == 15:
        print("*")
        return
    print("x")


if __name__ == '__main__':
    main()
