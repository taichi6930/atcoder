import collections
from bisect import bisect_left


def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    Ad = collections.deque(sorted(list(set(A))))

    for a in A:
        print(bisect_left(Ad, a))


if __name__ == '__main__':
    main()
