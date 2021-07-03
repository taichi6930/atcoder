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
    S = list(input())
    n = len(S)
    ans = 2 * (n - 1)

    for i in range(1, n - 1):
        swi = 2 if S[i] == "U" else 1
        ans += swi * (i) + (3 - swi) * (n - i - 1)

    print(ans)


if __name__ == '__main__':
    main()
