import math


import collections


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
