import math
import sys
from collections import Counter
readline = sys.stdin.readline


def main():
    n, k = map(int, readline().rstrip().split())
    a = list(map(int, readline().rstrip().split()))
    c = Counter(a)
    print(sum(sorted(c.values(), reverse=True)[k: len(c)]))


if __name__ == '__main__':
    main()
