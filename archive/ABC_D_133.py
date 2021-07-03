import math
import sys
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    A = list(map(int, readline().rstrip().split()))
    k = [0] * (n + 1)
    for i in range(n):
        k[i] += A[i] // 2
        k[i + 1] += A[i] // 2
    print(k)


if __name__ == '__main__':
    main()
