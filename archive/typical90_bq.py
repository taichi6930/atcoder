def mul(a, b):
    return ((a % mod) * (b % mod)) % mod


def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, y/2)**2 % mod
    else:
        return power(x, y/2)**2 * x % mod


def div(a, b):
    return mul(a, power(b, mod-2))


n, k = map(int, input().split())
mod = 10 ** 9 + 7
if n == 1:
    print(k)
elif n == 2:
    print(k * (k - 1))
else:
    print((k * (k - 1) * (k - 2) ** (n - 2)) % mod)
