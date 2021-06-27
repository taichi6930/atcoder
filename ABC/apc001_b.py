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
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(n):
        if A[i] > B[i]:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    main()
