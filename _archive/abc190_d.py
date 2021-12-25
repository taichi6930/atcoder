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
    divide_list = make_divisors(2 * n)
    dn = len(divide_list)
    ans = 0

    for i in range(len(divide_list)):
        k = divide_list[i]
        l = divide_list[dn - i - 1]
        if (l + k - 1) % 2 == 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
