import math
from itertools import accumulate


mod = 10 ** 9 + 7


def main():
    n = int(input())
    C = sorted(list(map(int, input().split())))
    ans = 1
    for i in range(n):
        d = C[i] - i
        if d <= 0:
            ans = 0
            break
        ans *= (C[i] - i) % mod
        ans = ans % mod

    print(ans % mod)


if __name__ == '__main__':
    main()
