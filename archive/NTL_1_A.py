
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


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


def main():
    n = int(input())
    print(str(n) + ": " + " ".join(int2strWithArray(prime_factorization(n))))


if __name__ == '__main__':
    main()
