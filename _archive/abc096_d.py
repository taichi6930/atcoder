from collections import deque
n = int(input())


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


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
    import math

    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


ans = deque()
cnt = 0
for i in range(5556):
    if is_prime(i * 10 + 3):
        ans.append(i * 10 + 3)
        cnt += 1
    if cnt >= n:
        break

print(' '.join(int2strWithArray(ans)))
