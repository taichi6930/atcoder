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
    n = int(input())
    s = list(input())
    t = list(input())
    a = 0
    for i in range(n):
        if "".join(s[n - i - 1:]) == "".join(t[0: i + 1]):
            a = i + 1
    print(2 * n - a)


if __name__ == '__main__':
    main()
