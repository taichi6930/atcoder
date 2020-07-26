import sys
import collections
import bisect
import math
readline = sys.stdin.readline


def main():
    r, g, b, n = map(int, readline().rstrip().split())
    cnt = 0
    for rr in range(math.ceil(n / r)):
        print(n - rr * r)


if __name__ == '__main__':
    main()
