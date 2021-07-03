import collections
import math
from itertools import accumulate
from bisect import bisect_left
from copy import deepcopy

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
    A = [0] + list(map(int, input().split()))
    Alist = [1]
    Blist = []

    ans = 0
    an2 = 0

    for i in range(min(k, 2 * 10 ** 5)):
        # Alistにあった場合
        if A[Alist[i]] in Alist:
            AlistStart = Alist.index(A[Alist[i]])
            Blist = Alist[AlistStart:]
            print(Alist, Blist)
            # 既にここまでlen(Alist)だけ消化している
            # n - len(Alist)のうち、len(Blist)の倍数は消化される
            q = (k - len(Alist)) % len(Blist)

            # Blistのk番目を取得
            print(Blist[q])
            return
            # Alistになければappend
        Alist.append(A[Alist[i]])

    print(Alist[-1])


if __name__ == '__main__':
    main()
