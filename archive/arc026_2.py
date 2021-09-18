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
    a = make_divisors(n)
    sumA = sum(a) - n
    ans = sumA - n

    if ans == 0:
        print("Perfect")
    elif ans > 0:
        print("Abundant")
    elif ans < 0:
        print("Deficient")


if __name__ == '__main__':
    main()
