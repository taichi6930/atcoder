import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n, m = map(int, readline().rstrip().split())
    print(abs((m - 2) * (n - 2)))


if __name__ == '__main__':
    main()
