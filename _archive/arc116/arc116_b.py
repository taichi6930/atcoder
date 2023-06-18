n = int(input())
A = sorted(list(map(int, input().split())))

mod = 998244353
s = A[0]
ans = sum([pow(a, 2, mod) for a in A]) % mod

for i in range(1, n):
    ans = (ans + s * A[i]) % mod
    s = (2 * s + A[i]) % mod

print(ans % mod)
