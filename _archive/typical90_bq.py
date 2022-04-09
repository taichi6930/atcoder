n, k = map(int, input().split())

mod = 10 ** 9 + 7


def power_mod(n, k, _mod=mod):
    # n ** kの余を計算する
    result = 1
    for i in range(10 ** 20):
        if k <= 0:
            break
        if (k & 1) == 1:
            result = (result * n) % _mod
        n = n * n % _mod
        k >>= 1
    return result


ans = (k * (k - 1) % mod) * power_mod(max(0, k - 2), (n - 2), mod)

print(ans % mod)
