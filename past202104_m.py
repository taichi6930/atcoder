import datetime
import collections
import math
from itertools import accumulate  # 累積和を求めるときに使う
from itertools import permutations  # 順列全探索で使う
from bisect import bisect_left
from pprint import pprint

mod = 10 ** 9 + 7
alphaList = list("abcdefghijklmnopqrstuvwxyz")
mod2 = 998244353


def is_prime(n):
    """
    数字が素数かどうかを判定する

    Parameters
    ----------
    n : int
        素数かどうかを求めたい数

    Returns
    -------
    boolean
        素数であればTrue
    """
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


def prime_factorization(n):  # 素因数分解を行う
    """
    task:prime factorization
    return:prime
    type:list
    """
    lis = []
    for i in range(2, int(n ** 0.5) + 1):
        while True:
            if n % i == 0:
                lis.append(i)
                n = n // i

            else:
                break

    if n > int(n ** 0.5):
        lis.append(n)

    return lis


def str2intWithArray(Array):  # 文字の配列を数字の配列に変換する
    return list(map(lambda x: int(x), Array))


def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


def cmb(n, r, m=None):  # 組み合わせ計算
    from functools import reduce
    from operator import mul

    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    if m is None:
        return over // under
    return (over // under) % m


# 等差数列の和（初項、末項、公差）
def get_sum_of_arithmetic_progressions(n, a, l=None, d=None):
    try:
        if (d is not None and l is not None):
            raise NameError('d is not None and l is not None')
        if (d is None and l is None):
            raise NameError('d is None and l is None')
        if l is not None:
            return (a + l) * n // 2
        return (2 * a + (n - 1) * d) * n // 2
    except NameError as e:
        print(e)
        exit()


def main():
    pass


if __name__ == '__main__':
    main()
