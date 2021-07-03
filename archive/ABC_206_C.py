import math
import collections


def main():
    n = int(input())
    q = n * (n - 1) // 2

    A = sorted(list(map(int, input().split())))
    c = collections.Counter(A)

    for i in c.values():
        q -= i * (i - 1)//2

    print(q)


if __name__ == '__main__':
    main()
