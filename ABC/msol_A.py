import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    x = int(readline().rstrip())
    li = [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
    for i in range(9):
        if li[i] > x:
            print(9 - i)
            break


if __name__ == '__main__':
    main()
