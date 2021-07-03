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
    n = int(input())
    for a in range(1, 100):
        if n <= 3 ** a:
            break
        for b in range(1, 100):
            if n < 3 ** a + 5 ** b:
                break
            if n == 3 ** a + 5 ** b:
                print(a, b)
                return
    print(-1)


if __name__ == '__main__':
    main()
