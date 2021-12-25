import math
import collections


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
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    B = set()

    for a in A:
        B |= set(make_divisors(a))
    B = list(B)
    C = collections.deque([1])
    for i in range(2, m + 1):
        if i in B:
            continue
        if not(is_prime(i)):
            D = set(prime_factorization(i))
            if len(D) == 1:
                continue
            swi = False
            for d in D:
                if not(d in C):
                    swi = True
                    break
            if swi:
                continue
        C.append(i)
    print(len(C))
    for c in C:
        print(c)


if __name__ == '__main__':
    main()
