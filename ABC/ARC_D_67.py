import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n, a, b = map(int, readline().rstrip().split())
    x = list(map(int, readline().rstrip().split()))
    sumX = 0
    for i in range(n-1):
        sumX += min(b, a * (x[i + 1] - x[i]))
    print(sumX)


if __name__ == '__main__':
    main()
