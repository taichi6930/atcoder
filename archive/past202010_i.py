from itertools import accumulate  # 累積和を求めるときに使う
from bisect import bisect_left


def main():
    n = int(input())
    A = list(map(int, input().split()))
    k = list(accumulate(A))
    sumA = sum(A)
    acc = [0] + list(accumulate(A)) + \
        list(map(lambda x: x + sumA, list(accumulate(A))))

    ans = sumA
    for i in range(n):
        l = sumA + acc[i] * 2
        B = list(map(lambda x: x * 2, acc[i + 1: i + n + 1]))
        x = bisect_left(B, l)
        C = list(map(lambda x: abs(x - l),
                 B[max(0, x - 1): min(n - 1, x + 1)]))
        ans = min(ans, min(C))

    print(ans == int(input()))


if __name__ == '__main__':
    main()
