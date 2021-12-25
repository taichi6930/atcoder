def main():
    x, y = map(int,  input().split())
    if ((x + y) % 3 != 0):
        print(0)
        return
    a, b = x - (x + y) // 3, y - (x + y) // 3
    print(conb(a + b, a))


mod = 10**9+7


def modpow(a, n):
    if n < 1:
        return 1
    ans = modpow(a, n//2)
    ans = (ans*ans) % mod
    if n % 2 == 1:
        ans *= a
    return ans % mod


def conb(n, i):
    inv, ans = 1, 1
    for j in range(1, i+1):
        ans = ans*(n-j+1) % mod
        inv = inv*j % mod
    return (ans*modpow(inv, mod-2)) % mod


if __name__ == '__main__':
    main()
