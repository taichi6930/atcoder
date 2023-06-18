from itertools import accumulate  # 累積和を求めるときに使う


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] + list(accumulate(A))
    for i in range(n - k + 1):
        print(B[k + i] - B[i])


if __name__ == '__main__':
    main()
