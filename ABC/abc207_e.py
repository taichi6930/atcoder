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
    A = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        B = A[i + 1:n]
        if len(B) == 0:
            ans = (ans + 1) % mod
        print(B)
        for j in range(i + 1, n):
            pass


if __name__ == '__main__':
    main()
