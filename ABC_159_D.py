import math
import sys
readline = sys.stdin.readline


def main():
    # input
    n = int(readline().rstrip())
    A = list(map(int, readline().rstrip().split()))
    B = [0] * n

    for a in A:
        B[a - 1] += 1

    total = 0
    for b in B:
        if b > 1:
            total += b * (b - 1) // 2

    C = [0] * n
    for i, b in enumerate(B):
        C[i] = total - b + 1

    for a in A:
        print(C[a-1])


if __name__ == '__main__':
    main()
