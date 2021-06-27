import collections
import math

mod = 10 ** 9 + 7
alphaList = list("abcdefghijklmnopqrstuvwxyz")


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    a, b, c, d = map(int, input().split())
    for i in range(16):
        s, t = [], []
        num = i
        if num >= 8:
            s.append(a)
            num -= 8
        else:
            t.append(a)
        if num >= 4:
            s.append(b)
            num -= 4
        else:
            t.append(b)
        if num >= 2:
            s.append(c)
            num -= 2
        else:
            t.append(c)
        if num >= 1:
            s.append(d)
            num -= 1
        else:
            t.append(d)
        if sum(s) == sum(t):
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
