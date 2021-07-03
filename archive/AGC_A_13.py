import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    A = list(map(int, readline().rstrip().split()))

    diff = 0
    cnt = 1

    for a in range(len(A) - 1):
        diffnow = 0


if __name__ == '__main__':
    main()
