import sys
import collections
import bisect


def main():
    n = int(input())
    k = 1
    for i in range(1, n):
        k *= i

    xyList = [list(map(int, input().split())) for _ in range(n)]
    xyListSum = 0
    for xn in range(1, n):
        for yn in range(xn + 1, n + 1):
            xyListSum += ((xyList[xn-1][0] - xyList[yn-1][0]) **
                          2 + (xyList[xn-1][1] - xyList[yn-1][1]) ** 2) ** 0.5
    print((2 * xyListSum) / k)


if __name__ == '__main__':
    main()
