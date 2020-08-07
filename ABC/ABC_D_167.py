import math
import sys
readline = sys.stdin.readline


def main():
    n, k = map(int, readline().rstrip().split())
    a = list(map(int, readline().rstrip().split()))
    kiroku = [-1] * n
    for i in range(n):
        print(a[i]-1, kiroku[a[i]-1])
        if kiroku[a[i]-1] == -1:
            kiroku[a[i] - 1] = i
        else:
            break
    print(kiroku)


if __name__ == '__main__':
    main()
