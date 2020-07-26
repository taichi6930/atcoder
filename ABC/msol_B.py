import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    a, b, c = map(int, readline().rstrip().split())
    k = int(readline().rstrip())
    i = 0
    while k > i:
        if a >= b:
            b *= 2
            i += 1
            continue
        if b >= c:
            c *= 2
            i += 1
            continue
        print('Yes')
        return
    print('Yes' if c > b and b > a else 'No')


if __name__ == '__main__':
    main()
