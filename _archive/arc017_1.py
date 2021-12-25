from functools import reduce
from operator import mul
from itertools import accumulate  # 累積和を求めるときに使う
from itertools import permutations  # 順列全探索で使う


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
