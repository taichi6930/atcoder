import math
import sys
readline = sys.stdin.readline


def main():
    l, r, d = map(int, readline().rstrip().split())
    print(math.floor(r/d) - math.ceil(l/d) + 1)


if __name__ == '__main__':
    main()
