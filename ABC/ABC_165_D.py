import math
import sys
readline = sys.stdin.readline


def main():
    a, b, n = map(int, readline().rstrip().split())
    maxt = 0
    for x in range(n):
        maxt = max(maxt, math.floor(a * (x + 1) / b) -
                   a * math.floor((x+1) / b))
    print(maxt)


if __name__ == '__main__':
    main()
