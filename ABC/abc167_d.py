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
    n, k = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    Alist = [1]

    for i in range(min(k, 2 * 10 ** 5)):

        Alist.append(A[Alist[i]])
    # print(Alist)


if __name__ == '__main__':
    main()
