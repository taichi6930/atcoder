def Base_10_to_n(X, n):  # 10進法からn進法に変換
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X % n)
    return str(X % n)


def Base_n_to_10(X, n):  # n進法から10進法に変換
    X = str(X)[::-1]
    s = 0
    for i in range(len(X)):
        s += int(X[i]) * n ** i
    return s


n, k = map(int, input().split())

for i in range(k):
    n = Base_n_to_10(n, 8)
    n = Base_10_to_n(n, 9).replace('8', '5')

print(n)
