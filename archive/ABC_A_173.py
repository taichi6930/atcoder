import math
import sys
from collections import Counter
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    while n > 0:
        n -= 1000
    print(-n)


if __name__ == '__main__':
    main()
