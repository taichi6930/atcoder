import collections
import sys
readline = sys.stdin.readline


def main():
    k, n = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    minA = 10 ** 7

    for i in range(n):
        minA = min(minA, A[i % n])


if __name__ == '__main__':
    main()
