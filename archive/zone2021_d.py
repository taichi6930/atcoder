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
    S = list(input())
    n = len(S)
    T = []
    swi = 1

    for s in S:
        if s == "R":
            swi *= -1
            continue

        if swi == 1:
            T = T + [s]
            continue

        if swi == -1:
            T = [s] + T
            continue

    if swi == -1:
        T.reverse()

    cnt = 0
    for i in range(10 ** 8):
        if cnt + 1 >= len(T):
            break
        if T[cnt] != T[cnt + 1]:
            cnt += 1
            continue

        T.pop(cnt + 1)
        T.pop(cnt)

        if cnt == 0:
            cnt += 2
            continue
        cnt -= 1

    print("".join(T))


if __name__ == '__main__':
    main()
