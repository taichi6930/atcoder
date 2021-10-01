def make_divisors(n):
    """
    約数列挙を行う。

    Parameters
    ----------
    n : int
        約数を求めたい数

    Returns
    -------
    divisors : [int]
        約数が昇順に入った配列
    """
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    divisors = lower_divisors + upper_divisors[::-1]
    return divisors


def main():
    x, y = map(int, input().split())
    cntx = len(make_divisors(x))
    cnty = len(make_divisors(y))
    if cntx > cnty:
        print('X')
        return
    if cntx < cnty:
        print('Y')
        return
    print('Z')


if __name__ == '__main__':
    main()
