import collections


def prime_factorization(n):
    """
    task:prime factorization
    return:prime
    type:list
    """
    lis = []
    for i in range(2, int(n ** 0.5) + 1):  # 割り算のTryは2から、平方根以下まで
        while True:
            if n % i == 0:
                lis.append(i)  # 余り0なら素因数分解リストにappendする
                n = n // i  # nの更新

            else:
                break

    if n > int(n ** 0.5):  # nがint(n**0.5) より大きなポイントでbreakしていたらそれをリストにappend 素数の時もこれ
        lis.append(n)

    return lis


def main():
    n = int(input())
    A = []
    for i in range(2, n + 1):
        A += prime_factorization(i)
    C = collections.Counter(A)

    ans = 0
    p75, p25, p15, p5, p3 = 0, 0, 0, 0, 0

    for j in C.values():
        if j >= 2:
            p3 += 1
        if j >= 4:
            p5 += 1
        if j >= 14:
            p15 += 1
        if j >= 24:
            p25 += 1
        if j >= 74:
            p75 += 1

    ans += (p5 * (p5 - 1) // 2) * (p3 - 2)
    ans += p25 * (p3 - 1)
    ans += p15 * (p5 - 1)
    ans += p75

    print(ans)


if __name__ == '__main__':
    main()
