import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    A = list(map(int, readline().rstrip().split()))

    if n < 3:
        print(1)
        return

    cnt = 1
    for i in range(n - 2):
        if (A[i + 1] - A[i]) * (A[i + 2] - A[i + 1]) < 0:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
