m, n, N = map(int, input().split())
ans = N
q = 0

for i in range(1000):
    p = (N // m) * n
    q += N - (N // m) * m
    p += (q // m) * n
    ans += p
    q = q - (q // m) * m
    N = p
    if N == 0:
        break

print(ans)
