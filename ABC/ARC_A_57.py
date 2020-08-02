import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    a, k = map(int, readline().rstrip().split())
    t = a
    cnt = 0
    while t < 2 * 10 ** 12:
        cnt += 1
        t += 1 + k * t
    print(cnt)


if __name__ == '__main__':
    main()
