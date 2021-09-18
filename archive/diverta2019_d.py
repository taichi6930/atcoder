def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    n = int(input())
    ans = 0

    A = make_divisors(n)

    for a in A:
        if n // a < 2:
            break
        if n % a != 0:
            continue
        m = n // a - 1
        if m <= a:
            break
        ans += m
    print(ans)


if __name__ == '__main__':
    main()
