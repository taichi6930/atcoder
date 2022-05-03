from math import gcd
mod = 10 ** 9 + 7

n = int(input())
A = list(map(int, input().split()))

lcm = 1

for i in range(n):
    lcm = lcm * A[i] // gcd(lcm, A[i])

ans = 0
for i in range(n):
    ans += lcm * pow(A[i], mod-2, mod)
    ans %= mod

print(ans)
