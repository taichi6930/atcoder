import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
	x, y = map(int, readline().rstrip().split())
	print((max(0, 4 - x) + max(0, 4 - y) + max(0, 2 - x * y) * 4) * 100000)

if __name__ == '__main__':
    main()
