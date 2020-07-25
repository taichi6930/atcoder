import math
import sys
from collections import Counter
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    s = [readline().rstrip() for _ in range(n)]
    c = Counter(s)
    lis = ['AC', 'WA', 'TLE', 'RE']
    for li in lis:
        print(li+' x ' + str(c[li]))


if __name__ == '__main__':
    main()
