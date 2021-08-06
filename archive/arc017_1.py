from functools import reduce
from operator import mul
import collections

from itertools import accumulate  # 累積和を求めるときに使う
from itertools import permutations  # 順列全探索で使う
from bisect import bisect_left

mod = 10 ** 9 + 7
alphaList = list("abcdefghijklmnopqrstuvwxyz")
mod2 = 998244353


def is_prime(n):
    import math
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    print("YES" if is_prime(int(input())) else "NO")


if __name__ == '__main__':
    main()
