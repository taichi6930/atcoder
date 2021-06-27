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
    ans = 10 ** 10
    n = int(input())
    A = list(map(int, input().split()))

    for i in range(n):
        A[i] -= (i + 1)
    avgA = int(round((sum(A) / n), 0))

    for a in range(avgA - 10, avgA + 10):
        ansK = 0
        for j in range(n):
            ansK += abs(A[j] - a)
        ans = min(ans, ansK)
    print(ans)


if __name__ == '__main__':
    main()
