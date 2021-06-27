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
    n = int(input())
    S = [list(input()) for _ in range(n)]
    C = [collections.Counter(S[a]) for a in range(n)]

    ansList = []

    for key in C[0].keys():
        num = 100
        for i in range(n):
            num = min(C[i][key], num)
            if num == 0:
                break
        ansList += [key] * num
    print("".join(sorted(ansList)))


if __name__ == '__main__':
    main()
