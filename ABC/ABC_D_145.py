import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    x, y = map(int, readline().rstrip().split())
    if ((x + y) % 3 != 0):
        print(0)
        return


if __name__ == '__main__':
    main()
