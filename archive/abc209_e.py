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


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    top = list(map(lambda x: x[0:3], s))
    tail = list(map(lambda x: x[-3:], s))

    winS = []

    for j in range(n):
        if not tail[j] in top:
            winS.append(s[j])
            continue

    for a in range(n):
        ss = s[a]
        if ss[0:3] == ss[-3:]:
            print("Draw")
        elif not ss[-3:] in top:
            print("Takahashi")
        else:
            print("Aoki")


if __name__ == '__main__':
    main()
