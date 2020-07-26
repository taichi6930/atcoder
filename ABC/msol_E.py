import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    xypList = [list(map(int, readline().rstrip().split())) for _ in range(n)]
    disList = [0] * n
    for i in range(n):
        xyp = xypList[i]
        disList[i] = min(xyp[0], xyp[1]) * xyp[2]
    print(xypList, disList)


if __name__ == '__main__':
    main()
