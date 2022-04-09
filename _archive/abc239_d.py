import math


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


def main():
    a, b, c, d = map(int, input().split())

    for i in range(a, b + 1):
        # False: 素数以外にできる = 高橋くんが勝ち
        swi = True
        for j in range(c, d + 1):
            if is_prime(i + j):
                swi = False
                break
        if swi:
            print('Takahashi')
            return

    print('Aoki')


if __name__ == '__main__':
    main()
