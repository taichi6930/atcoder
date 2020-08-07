import math
import sys
import collections
import bisect


def main():
    n = int(input())
    s = [0] + list(input()) + [0]
    for i in range(1, n + 1):
        print(s[i])


if __name__ == '__main__':
    main()
