import math
import sys
readline = sys.stdin.readline


def main():
    x, n = map(int, readline().rstrip().split())
    p = list(map(int, readline().rstrip().split()))
    for k in range(100):
        if p.count(x - k) == 0:
            print(x - k)
            break
        if p.count(x + k) == 0:
            print(x + k)
            break


if __name__ == '__main__':
    main()
