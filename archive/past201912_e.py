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
    n, q = map(int, input().split())
    ANS = [set() for _ in range(n + 1)]

    for i in range(q):
        S = list(map(int, input().split()))
        if S[0] == 1:
            a, b = S[1], S[2]
            ANS[a].add(b)
            continue

        if S[0] == 2:
            a = S[1]
            for i in range(n + 1):
                if a in ANS[i]:
                    ANS[a].add(i)

        if S[0] == 3:
            a = S[1]
            K = list(ANS[a])
            for k in K:
                ANS[a] = ANS[a] | ANS[k]

    ANS = ANS[1::]

    for j in range(n):
        ans = ''
        for z in range(1, n + 1):
            if z - 1 == j:
                ans += 'N'
                continue
            if z in ANS[j]:
                ans += 'Y'
                continue
            ans += 'N'
        print(ans)


if __name__ == '__main__':
    main()
