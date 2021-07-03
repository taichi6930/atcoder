import numpy as np
import collections
import math
from itertools import accumulate
from bisect import bisect_left
from copy import deepcopy
from scipy.special import comb

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


def idx_of_the_nearest(list, num):
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]


def main():
    n = int(input())
    A = list(map(int, input().split()))
    maxA = 0
    maxq, maxr = 0, 0
    for i in range(n):
        q = A[i]
        B = A[0: i] + A[i + 1:]
        r = idx_of_the_nearest(B, q / 2)
        ans = comb(q, r)
        if maxA <= ans:
            maxA = ans
            maxq = q
            maxr = r
    print(maxq, maxr)


if __name__ == '__main__':
    main()
