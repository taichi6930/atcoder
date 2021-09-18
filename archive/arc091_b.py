import math
from itertools import accumulate
from copy import deepcopy


def main():
    n, k = map(int, input().split())
    ans = 0
    for b in range(k + 2, n + 1):
        ans += (n // b) * (n - k) + max((n % b) - k, 0)
    print(ans)


if __name__ == '__main__':
    main()
