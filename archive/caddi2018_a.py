import collections


def prime_factorization(n):
    """
    task:prime factorization
    return:prime
    type:list
    """
    lis = []
    for i in range(2, int(n**0.5)+1):  # 割り算のTryは2から、平方根以下まで
        while True:
            if n % i == 0:
                lis.append(i)  # 余り0なら素因数分解リストにappendする
                n = n//i  # nの更新

            else:
                break

    if n > int(n**0.5):  # nが　int(n**0.5) より大きなポイントでbreakしていたらそれをリストにappend 素数の時もこれ
        lis.append(n)

    return lis


def main():
    ans = 1
    n, p = map(int, input().split())

    c = collections.Counter(prime_factorization(p))
    for key in c.keys():
        ans *= key ** (c[key] // n)
    print(ans)


if __name__ == '__main__':
    main()
