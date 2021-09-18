import math


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
