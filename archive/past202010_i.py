from itertools import accumulate  # 累積和を求めるときに使う
from bisect import *


def main():
    n = int(input())
    A = list(map(int, input().split()))

    # 後で削除する
    # A = [a for a in range(n)]
    import time
    st = time.perf_counter()

    sumA = sum(A)
    acc = [0] + list(accumulate(A)) + \
        list(map(lambda x: x + sumA, list(accumulate(A))))
    B = list(map(lambda x: x * 2, acc))
    l = 0
    print(B)

    ans = sumA
    for i in range(n):
        l += acc[i]
        x = bisect_left(B, l)
        if x <= i:
            x = i + 1
        if x >= i + n:
            x = i + n - 1
        ans = min(ans, abs(B[x] - l))
        y = bisect_right(B, l)
        if y <= i:
            y = i + 1
        if y >= i + n:
            y = i + n - 1
        ans = min(ans, abs(B[x] - l))
        print(ans, l)
    print(ans)

    print((time.perf_counter() - st))


if __name__ == '__main__':
    main()
