import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    A = [0 for _ in range(10 ** 5 + 1)]

    for i in range(1, 10 ** 5 + 1):
        A[i] = A[i - 1]
        if i % 2 == 0:
            continue

        if not is_prime(i):
            continue

        if not is_prime((i + 1) // 2):
            continue

        A[i] = A[i] + 1

    q = int(input())
    for i in range(q):
        l, r = map(int, input().split())
        print(A[r] - A[l - 1])


if __name__ == '__main__':
    main()
