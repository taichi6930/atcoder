from itertools import accumulate  # 累積和を求めるときに使う


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] + list(accumulate(A))
    for k in range(n):
        print(max([B[i + k + 1] - B[i] for i in range(n - k)]))


if __name__ == '__main__':
    main()
