import math
from bisect import bisect_left, bisect_right


def is_prime(n):
    """
    数字が素数かどうかを判定する

    Parameters
    ----------
    n : int
        素数かどうかを求めたい数

    Returns
    -------
    boolean
        素数であればTrue
    """
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


ans = 0
n = int(input())

prime_list = []

for i in range(2, min(n + 1, 300000)):
    if is_prime(i):
        prime_list.append(i)

for a in range(2, 10**3):
    if n < a**5:
        break
    if not is_prime(a):
        continue
    for b in range(a + 1, 10**4):
        if n < (a**2 * b):
            break
        if not is_prime(b):
            continue
        cmax = int((n / (a**2 * b)) ** 0.5)
        ans += max(0, bisect_right(prime_list, cmax) - bisect_left(prime_list, b + 1))
print(ans)
