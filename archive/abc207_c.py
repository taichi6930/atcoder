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
    n = int(input())
    lrList = [None] * n
    for i in range(n):
        t, l, r = map(int, input().split())
        if t == 1:
            lrList[i] = [l, r]
            continue
        if t == 2:
            lrList[i] = [l, r - 0.1]
            continue
        if t == 3:
            lrList[i] = [l + 0.1, r]
            continue
        if t == 4:
            lrList[i] = [l + 0.1, r - 0.1]
            continue

    ans = 0
    for j in range(n - 1):
        for k in range(j + 1, n):
            if min(lrList[j][1], lrList[k][1]) - max(lrList[j][0], lrList[k][0]) >= 0:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
