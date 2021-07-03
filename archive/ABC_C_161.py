import sys
import math
readline = sys.stdin.readline


def main():
    n, k = map(int, readline().rstrip().split())
    print(min(n % k, k - n % k))


if __name__ == '__main__':
    main()
