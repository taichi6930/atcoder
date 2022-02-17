from itertools import accumulate  # 累積和を求めるときに使う


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] + list(accumulate(A))

    for i in range(n + 1):
        B[i] = B[i] % 360
    B = sorted(B)

    ans = 0

    for j in range(n):
        ans = max(B[j + 1] - B[j], ans)

    print(max(ans, 360 - B[-1]))


if __name__ == '__main__':
    main()
