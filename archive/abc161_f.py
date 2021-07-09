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


def main():
    n = int(input())
    divisor = make_divisors(n)
    numDivisor = len(divisor)
    ansKList = []
    ans = 0

    for i in range(numDivisor):
        x1 = divisor[i]
        x2 = divisor[numDivisor - i - 1]

        bk = x2 - 1

        # kを求めることができる
        kList = make_divisors(bk)
        for k in kList:
            if k == 1:
                continue
                a = int(math.log(x1, k))
                if x1 == k ** a:
                    ans += 1
                    ansKList.append(k)

        # if bk == 0:
        #     # kは任意になる
        #     # n = k ** aとなるため、これを求める
        #     kList = make_divisors(n)
        #     for k in kList:
        #         if k == 1:
        #             continue
        #         a = int(math.log(x1, k))
        #         if x1 == k ** a:
        #             ans += 1
        #             ansKList.append(k)

    print(len(set(ansKList)))


if __name__ == '__main__':
    main()
