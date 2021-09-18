from bisect import bisect_left
import math
from itertools import accumulate
from math import copysign


def main():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(q):
        k = int(input())
        index = bisect_left(A, k)
        print(index, k)


if __name__ == '__main__':
    main()
