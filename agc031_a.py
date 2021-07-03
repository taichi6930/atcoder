import collections
import math

mod = 10 ** 9 + 7
alphaList = list("abcdefghijklmnopqrstuvwxyz")
mod2 = 998244353


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    n = int(input())
    S = list(input())
    ans = 1
    C = collections.Counter(S)
    for val in C.values():
        ans = (ans * (val + 1)) % mod
    print((ans - 1) % mod)


if __name__ == '__main__':
    main()
