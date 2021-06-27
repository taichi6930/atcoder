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
    N, M = map(int, input().split())

    g = math.gcd(N, M)
    n = N//g
    m = M//g
    S = input()
    T = input()
    ans = n * m * g
    for i in range(g):
        if S[i * n] != T[i * m]:
            ans = -1
    print(ans)


if __name__ == '__main__':
    main()
