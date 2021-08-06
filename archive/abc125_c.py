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
    A = list(map(int, input().split()))
    Bfrom0toX = [A[0]] + [None for _ in range(n - 1)]
    BfromYtoN = [None for _ in range(n - 1)] + [A[n - 1]]

    for i in range(1, n):
        Bfrom0toX[i] = math.gcd(A[i], Bfrom0toX[i - 1])
        BfromYtoN[n - 1 - i] = math.gcd(BfromYtoN[n - i], A[n - i])

    ans = 1

    Bfrom0toX = [0] + Bfrom0toX
    BfromYtoN = BfromYtoN + [0]

    for j in range(n):
        if Bfrom0toX[j] * BfromYtoN[j] == 0:
            ans = max(Bfrom0toX[j] + BfromYtoN[j], ans)
            continue
        ans = max(math.gcd(Bfrom0toX[j], BfromYtoN[j]), ans)
    print(ans)


if __name__ == '__main__':
    main()
