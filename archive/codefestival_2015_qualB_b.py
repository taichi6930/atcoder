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
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    C = collections.Counter(A)
    # 1種類であれば答えはA[0]
    if len(C.keys()) == 1:
        print(A[0])
        return

    no1value = C.most_common()[0][1]
    no2value = C.most_common()[1][1]

    # no1の数が過半数超えていなかったら?になる
    if no1value <= n / 2 or no2value >= n / 2:
        print("?")
        return

    print(C.most_common()[0][0])


if __name__ == '__main__':
    main()