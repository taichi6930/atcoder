n, k, m = map(int, input().split())
mod = 998244353

print(pow(m, pow(k, n, mod - 1), mod) if m % mod != 0 else 0)
