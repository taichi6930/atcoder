import math
import sys
readline = sys.stdin.readline


def main():
    a, b = map(str, readline().rstrip().split())
    print((int(int(a) * float(b) * 100)) // 100)


if __name__ == '__main__':
    main()
