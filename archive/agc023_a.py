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
    A = list(map(int, input().split()))
    B = [0] + [None] * n

    for i in range(n):
        B[i + 1] = B[i] + A[i]

    C = collections.Counter(B)

    ans = 0

    for key in C.keys():
        ans += C[key] * (C[key] - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
