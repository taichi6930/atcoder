import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(input())
    cnt = 0
    if n < 300:
        print(0)
    for i in range(300, n + 1):
        nList = list(str(i))
        c = collections.Counter(nList)
        if c["3"] > 0 and c["5"] > 0 and c["7"] > 0:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
