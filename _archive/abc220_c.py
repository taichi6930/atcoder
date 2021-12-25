from itertools import accumulate  # 累積和を求めるときに使う
from bisect import bisect_right


def main():
    n = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    print((X // sum(A)) * n +
          bisect_right([0] + list(accumulate(A)), X % sum(A)))


if __name__ == '__main__':
    main()
