import math
import sys
readline = sys.stdin.readline


def main():
    n, m = map(int, readline().rstrip().split())
    aList = sorted(list(map(int, readline().rstrip().split())), reverse=True)
    aSum = sum(aList)
    mLine = aSum / (4 * m)
    print("Yes" if aList[m - 1] >= mLine else "No")


if __name__ == '__main__':
    main()
