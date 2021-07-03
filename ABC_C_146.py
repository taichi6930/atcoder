import math
import sys
import time
readline = sys.stdin.readline


def main():
    a, b, x = map(int, input().split())
    l, r = 0, 10 ** 9 + 1
    while r - l > 1:
        m = (l + r)//2
        t = a * m + b * (len(str(m)))
        if t <= x:
            l = m
        else:
            r = m
    print(l)


if __name__ == '__main__':
    main()
