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
    s = list(input())
    k = int(input())

    ans = 0

    if len(set(s)) == 1:
        print(int((len(s) * k) // 2))
        return

    if len(s) == 1:
        print(k - 1)
        return

    for i in range(1, len(s)):
        if s[i] != s[i - 1] or s[i - 1] == 0:
            continue
        ans += 1
        s[i] = 0
    ans = ans * k
    if s[0] == s[-1]:
        ans += k - 1
    print(ans)


if __name__ == '__main__':
    main()
