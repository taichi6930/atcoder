import collections
from itertools import accumulate  # 累積和を求めるときに使う


def main():
    n, w = map(int, input().split())
    A = [0] * (10 ** 6)

    for _ in range(n):
        s, t, p = map(int, input().split())
        A[s] = A[s] + p
        A[t] = A[t] - p

    print("Yes" if w >= max(collections.Counter(
        list(accumulate(A))).keys()) else "No")


if __name__ == '__main__':
    main()
