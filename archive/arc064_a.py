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


def cnt_step(Arr, x):
    ans = 0

    n = len(Arr)

    for i in range(n):
        minus = max(0, Arr[i] - x)

        if minus == 0:
            continue

        ans += minus
        Arr[i] -= minus
        if i + 1 != n:
            Arr[i + 1] -= minus
    return ans


def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    B = [A[i] + A[i + 1] for i in range(n - 1)]
    C = [B[n - 2 - j] for j in range(n - 1)]

    print(min(int(cnt_step(B, x)), int(cnt_step(C, x))))


if __name__ == '__main__':
    main()
