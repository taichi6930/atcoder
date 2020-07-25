import math
import sys
import collections
import bisect
import sympy
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    sumN = 0
    for i in range(n):
        sumN += len(sympy.divisors(i + 1)) * (i + 1)
    print(sumN)


if __name__ == '__main__':
    main()
