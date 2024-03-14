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


k = int(input())
ans = 0
divisors = make_divisors(k)
lenDivisors = len(divisors)

for i in range(0, lenDivisors):
    a = divisors[i]
    if a ** 3 > k:
        break
    for j in range(i, lenDivisors):
        b = divisors[j]
        if a * b * b > k:
            break
        ab = a * b
        c = k // ab
        if k != ab * c:
            continue
        ans += 1

print(ans)
