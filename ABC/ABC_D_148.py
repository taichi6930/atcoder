import math
import sys
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    A = list(map(int, readline().rstrip().split()))
    k = -1
    for i in range(n):
        if k < A.index(i + 1):
            k = A.index(i + 1)
        else:
            print()


if __name__ == '__main__':
    main()
