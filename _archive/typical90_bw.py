import math
n = int(input())


def prime_factorization(n):  # 素因数分解を行う
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


def is_prime(n):
    """
    数字が素数かどうかを判定する

    Parameters
    ----------
    n : int
        素数かどうかを求めたい数

    Returns
    -------
    boolean
        素数であればTrue
    """
    import math

    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


print(0 if is_prime(n) else int(math.ceil(
    math.log(len(prime_factorization(n)), 2))))
