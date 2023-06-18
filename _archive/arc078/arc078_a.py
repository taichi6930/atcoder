from itertools import accumulate  # 累積和を求めるときに使う


def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 10 ** 10

    B = [0] + list(accumulate(A))
    for i in range(n - 1):
        x = B[i + 1] - B[0]
        y = B[-1] - B[i + 1]
        z = abs(x - y)
        ans = min(ans, z)

    print(ans)


if __name__ == '__main__':
    main()
