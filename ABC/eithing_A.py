import math
import sys
readline = sys.stdin.readline


def main():
    n = int(input())
    print((n - int(input()) + 1) * (n - int(input()) + 1))


if __name__ == '__main__':
    main()
