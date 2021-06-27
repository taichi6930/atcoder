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
    A = list(map(int, input().split()))
    A2 = [A[i] ** 2 for i in range(n)]
    print(sum(A2) // 2 - sum(A) ** 2)


if __name__ == '__main__':
    main()
