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
    n = int(input())
    cnt = 0
    for i in range(n):
        if (i + 1) % 2 == 0:
            continue
        if len(make_divisors(i + 1)) == 8:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
