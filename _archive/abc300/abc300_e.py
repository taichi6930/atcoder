n = int(input())


def prime_factorization(n):  # 素因数分解を行う
    """
    task:prime factorization
    return:prime
    type:list
    """
    lis = []
    for i in range(2, int(n**0.5) + 1):
        while True:
            if n % i == 0:
                lis.append(i)
                n = n // i

            else:
                break

    if n > int(n**0.5):
        lis.append(n)

    return lis
