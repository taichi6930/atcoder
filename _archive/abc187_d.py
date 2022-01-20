import collections
from itertools import accumulate  # 累積和を求めるときに使う
from bisect import bisect_right


def main():
    n = int(input())
    vort = 0
    AB = collections.deque()
    for _ in range(n):
        a, b = map(int, input().split())
        vort += a
        AB.append(a * 2 + b)
    print(bisect_right([0] + list(accumulate(sorted(AB, reverse=True))), vort))


if __name__ == '__main__':
    main()
