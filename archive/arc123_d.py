from functools import reduce
from operator import mul
import collections
import math
from itertools import accumulate  # 累積和を求めるときに使う
from itertools import permutations  # 順列全探索で使う
from bisect import bisect_left


def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [None for _ in range(n)]
    C = [None for _ in range(n)]
    D = [None for _ in range(n)]

    ans = 0

    B[0] = 0
    C[0] = 0
    D[0] = A[0] - B[0] - C[0]

    ans += abs(D[0])

    for i in range(1, n):
        B[i] = B[i - 1]
        C[i] = C[i - 1]
        D[i] = A[i] - B[i] - C[i]

        if D[i] >= D[i - 1]:
            ans += abs(B[i]) + abs(C[i]) + abs(D[i])
            continue

        if D[i] >= 0:
            B[i] += D[i]
            D[i] -= D[i]
            ans += abs(B[i]) + abs(C[i]) + abs(D[i])
            continue

        if D[i] < 0:
            C[i] += D[i]
            D[i] -= D[i]
            ans += abs(B[i]) + abs(C[i]) + abs(D[i])
            continue

    B = list(map(lambda x: abs(x), B))
    C = list(map(lambda x: abs(x), C))
    D = list(map(lambda x: abs(x), D))
    print(sum(B) + sum(C) + sum(D))


if __name__ == '__main__':
    main()
