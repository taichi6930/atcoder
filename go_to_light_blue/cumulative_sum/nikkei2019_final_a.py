def main():
    n = int(input())
    A = list(map(int, input().split()))

    # 累積和のためのリスト作成
    B = [0 for _ in range(n + 1)]
    for i in range(n):
        B[i + 1] = B[i] + A[i]

    # k個離れた数の和の最大値を出す
    for k in range(n):
        ans = 0
        print(max(B[j + k + 1] - B[j] for j in range(n - k)))


if __name__ == '__main__':
    main()
