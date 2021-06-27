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
    k = int(input())
    ans = 0
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            c = math.floor(k / a / b)
            if c <= 0:
                break
            ans += c
    print(ans)


if __name__ == '__main__':
    main()
