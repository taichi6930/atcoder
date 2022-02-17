
mod2 = 998244353


def main():
    n = int(input())

    # 全ての数を計算する
    ans = 0

    for i in range(1, len(str(n)) + 1):
        # 最後の数の桁の時、その分だけ引き算をする
        if i == len(str(n)):
            k = n - 10 ** (i - 1) + 1
            ans = (ans + ((k + 1) * k // 2) % mod2) % mod2
            continue
        ans = (ans + ((1 + 10 ** (i - 1) * 9) *
               (10 ** (i - 1) * 9) // 2) % mod2) % mod2

    print(ans)


if __name__ == '__main__':
    main()
