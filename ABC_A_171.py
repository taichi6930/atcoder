import math
import sys
from collections import Counter
readline = sys.stdin.readline


def main():
    s = readline().rstrip()
    print('A' if s.isupper() else 'a')


if __name__ == '__main__':
    main()
