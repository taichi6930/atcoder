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
    n, x, m = map(int, input().split())
    aList = [x]
    aNum = -1
    ans = 0

    for i in range(n - 1):
        # 元の値
        An = aList[-1]
        # Anの値
        An1 = An ** 2 % m

        if An1 in aList:
            aNum = aList.index(An1)
            a = An1
            break
        aList.append(An1)
    # まず今まで求めたものを全て足す
    ans += sum(aList)

    if aNum != -1:
        bList = aList[aNum:]
        bListLen = len(bList)

        # 繰り返し足し算するところを求める
        k = (n - len(aList)) // (bListLen)
        ans += sum(bList) * k

        l = n - len(aList) - bListLen * k
        ans += sum(bList[0:l])

    print(ans)


if __name__ == '__main__':
    main()
