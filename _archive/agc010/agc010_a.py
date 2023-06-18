import collections
from math import copysign


def main():
    n = int(input())
    A = list(map(lambda x: int(copysign(x % 2, x)),
                 list(map(int, input().split()))))
    C = collections.Counter(A)
    print("YES" if C[1] % 2 == 0 or (C[1] % 2 == 1 and C[0] == 0) else "NO")


if __name__ == '__main__':
    main()
