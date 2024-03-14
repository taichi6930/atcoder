n = int(input())
A = list(map(int, input().split()))
mod = 10**9 + 7
print(sum([a * pow(2, i, mod) for i, a in enumerate(A)]) % mod)
