import collections
import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    n, m = map(int, input().split())
    ans = 1
    for i in range(2, m):
        k = m - i * (n - 1)
        gcd = math.gcd(k, i)
        if gcd == 1 or ans > gcd:
            break
        ans = max(ans, gcd)
    print(ans)


if __name__ == '__main__':
    main()
