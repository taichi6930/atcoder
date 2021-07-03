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
    a, b, c = map(int, input().split())
    Z = [0, 1, 5, 6]

    #　そもそも最初の段階で0であれば終了
    if a % 10 in Z:
        print(a % 10)
        return

    A = [1]

    for i in range(10):
        k = (A[i] * a) % 10
        # if k in A:

        A.append(k)

    print(A)


if __name__ == '__main__':
    main()
