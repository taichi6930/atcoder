import collections
import math
from itertools import accumulate
from bisect import bisect_left


mod = 10 ** 9 + 7
alphaList = list("abcdefghijklmnopqrstuvwxyz")
mod2 = 998244353


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def make_divisors(n):
    """
    約数列挙を行う。

    Parameters
    ----------
    n : int
        約数を求めたい数

    Returns
    -------
    divisors : [int]
        約数が昇順に入った配列
    """
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    divisors = lower_divisors + upper_divisors[::-1]
    return divisors


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
    n, k = map(int, input().split())
    arrayN = list(map(lambda x: int(x), list(str(n))))
    lenN = len(arrayN)

    ans = 0

    if n < 10:
        print(min(k, n))
        return

    # 制限のないところは全部行える（nの桁数以下）
    # 0を含んだ計算
    ans += 10 ** (lenN - 1) - 9 ** (lenN - 1) + min(k, 9) - 1

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(2, len(arrayN)):
        cnt = 0
        B = []
        for j in range(1, 10):
            for a in A:
                q = a * j
                print(q, a, j)
                if q <= k and q % 10 != 0:
                    B.append(q)
                    cnt += 1
        print(B)
        ans += len(B)
        A = B
    print(ans)


if __name__ == '__main__':
    main()
