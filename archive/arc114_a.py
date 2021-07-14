import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def is_nth_bit_set(num: int, n: int):
    if num & (1 << n):
        return True
    return False


def main():
    ans = 1
    primeList = []
    for i in range(2, 51):
        if is_prime(i):
            primeList.append(i)
            ans *= i

    n = int(input())
    X = list(map(int, input().split()))

    for j in range(2 ** len(primeList)):
        a = 1
        for k in range(len(primeList)):
            if is_nth_bit_set(j, k):
                a *= primeList[k]
                if ans < a:
                    break

        if ans < a:
            continue
        swi = 1
        for x in X:
            if math.gcd(x, a) == 1:
                swi = 0
                break
        if swi == 1:
            ans = min(ans, a)
    print(ans)


if __name__ == '__main__':
    main()
