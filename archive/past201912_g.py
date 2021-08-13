from collections import deque
from pprint import pprint
from functools import reduce
from operator import mul
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
    A = [[0 for _ in range(i + 1)] +
         list(map(int, input().split())) for i in range(n - 1)]
    ans = None
    for i in range(3 ** (n + 1)):
        k = 0
        a0, a1, a2 = deque(), deque(), deque()
        q = i * 1
        if q % 3 != 0:
            continue
        for j in range(1, n + 1):

            if q % 3 == 0:
                a0.append(j)
            elif q % 3 == 1:
                a1.append(j)
                q -= 1
            elif q % 3 == 2:
                a2.append(j)
                q -= 2
            q = q // 3

        lena0, lena1, lena2 = len(a0), len(a1), len(a2)

        if lena0 > 1:
            for a0s in range(lena0 - 1):
                for a0f in range(a0s + 1, lena0):
                    k += A[a0[a0s] - 1][a0[a0f] - 1]

        if lena1 > 1:
            for a1s in range(lena1 - 1):
                for a1f in range(a1s + 1, lena1):
                    k += A[a1[a1s] - 1][a1[a1f] - 1]

        if lena2 > 1:
            for a2s in range(lena2 - 1):
                for a2f in range(a2s + 1, lena2):
                    k += A[a2[a2s] - 1][a2[a2f] - 1]
        if ans is None:
            ans = k
        ans = max(ans, k)
    print(ans)


if __name__ == '__main__':
    main()
