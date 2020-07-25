import math
import sys
readline = sys.stdin.readline


def main():
    x = int(readline().rstrip())
    print((x // 500) * 1000 + ((x - (x // 500) * 500) // 5) * 5)


if __name__ == '__main__':
    main()
