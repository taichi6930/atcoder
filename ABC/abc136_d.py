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
    s = list(input())
    n = len(s)
    L, R = [0] * (n + 1), [0] * (n + 1)
    for i in range(n):
        L[i + 1] = L[i]
        R[i + 1] = R[i]
        if s[i] == "L":
            L[i + 1] += 1
        else:
            R[i + 1] += 1
    print(L, R)


if __name__ == '__main__':
    main()
