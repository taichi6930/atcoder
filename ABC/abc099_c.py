import collections
import math

alphaList = list("abcdefghijklmnopqrstuvwxyz")


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    n = int(input())
    cnt = 0
    # 9円
    a9 = int(math.log(n, 9))
    a6 = int(math.log(n, 6))
    for i in range(10 ** 9):
        if n >= 9 ** a9:
            n -= 9 ** a9
            cnt += 1
            continue
        a9 -= 1
        if a9 <= 0:
            break
    print("cnt:", cnt)
    # 6円
    a6 = int(math.log(n, 6))
    for i in range(10 ** 9):
        if n >= 6 ** a6:
            n -= 6 ** a6
            cnt += 1
            continue
        a6 -= 1
        if a6 <= 0:
            break

    print(cnt + n)


if __name__ == '__main__':
    main()
