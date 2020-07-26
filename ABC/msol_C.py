import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n, k = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    for i in range(n - k):
        print('Yes' if A[k+i] > A[i] else 'No')


if __name__ == '__main__':
    main()
