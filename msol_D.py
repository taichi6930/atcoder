import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    A = list(map(int, readline().rstrip().split()))
    sumA = 0
    money = 1000
    for i in range(n - 1):
        if A[i + 1] - A[i] > 0:
            money += (A[i + 1] - A[i]) * math.floor(money / A[i])
    print(money)


if __name__ == '__main__':
    main()
