from pprint import pprint
import datetime
import collections
import math
from itertools import accumulate  # 累積和を求めるときに使う
from itertools import permutations  # 順列全探索で使う
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


def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


def cmb(n, r, m=None):
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


def main():
    n = int(input())
    S = [list(input()) for _ in range(n)]
    T = [['#' for _ in range(2 * n - 1)] for _ in range(n - 1)] + [S[-1]]

    for i in range(n - 1):
        a = n - i - 2
        for j in range(2 * n - 1):
            if S[a][j] == '.':
                T[a][j] = '.'
                continue
            if S[a][j] == 'X':
                T[a][j] = 'X'
                continue
            if 'X' in S[a + 1][max(0, j - 1):min(2 * n, j + 2)]:
                T[a][j] = 'X'
                continue

        S[a] = T[a]

    for k in range(n):
        print(''.join(T[k]))


if __name__ == '__main__':
    main()
