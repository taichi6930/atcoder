import collections
import math

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


def main():
    n, m = map(int, input().split())
    AList = []

    for i in range(m):
        x, y = map(int, input().split())
        if x in AList or len(AList) == 0:
            AList.append(y)
    print(len(set(AList)))


if __name__ == '__main__':
    main()
