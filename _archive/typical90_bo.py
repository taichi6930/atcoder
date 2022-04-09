# 16進数に対応するための辞書の作成
HEXA = '0123456789abcdef'
H_DIC = {HEXA[i]: i for i in range(16)}


def d2n(decimal_number, n):  # 10進数の decimal_number を n 進数に変換
    d, n = int(decimal_number), int(n)

    if (2 <= n <= 10) or n == 16:
        ans = ''
        while d:
            r = d % n
            ans = HEXA[r] + ans
            d = d // n
        return ans
    else:
        return False


def n2d(n, n_decimal_number):  # n 進数の n_decimal_number を 10進数に変換
    # n_decimal_number = str(n_decimal_number) は不要だが念のため
    n, n_decimal_number = int(n), str(n_decimal_number)
    if (2 <= n <= 10) or n == 16:
        ans = 0
        for figure in n_decimal_number:
            ans = ans * n + H_DIC[figure]
        return ans
    else:
        return False


def n2m(n, n_decimal_number, m):  # n 進数の n_decimal_number を m 進数に変換
    # n 進数 n_decimal_number を 10進数 tmp_10 に変換
    tmp_10 = n2d(n, n_decimal_number)
    # 10進数 tmp_10 を m 進数 ans に変換
    ans = d2n(tmp_10, m)
    return ans


n, k = map(int, input().split())

if n == 0:
    print(0)
    exit()

for i in range(k):
    n = str(n2m(8, n, 9)).replace('8', '5')

print(n)
