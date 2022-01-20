import collections
from itertools import accumulate  # 累積和を求めるときに使う


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] + list(accumulate(A))
    ans = 0
    C = collections.Counter([])

    for i in range(n):
        C[B[i]] = 1 + C[B[i]]
        ans += C[B[i + 1] - k]
    print(ans)


if __name__ == '__main__':
    main()
