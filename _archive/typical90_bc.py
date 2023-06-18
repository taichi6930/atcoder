n, p, q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for a1 in range(n - 4):
    k1 = A[a1] % p
    for a2 in range(a1 + 1, n - 3):
        k2 = (k1 * A[a2]) % p
        for a3 in range(a2 + 1, n - 2):
            k3 = (k2 * A[a3]) % p
            for a4 in range(a3 + 1, n - 1):
                k4 = (k3 * A[a4]) % p
                for a5 in range(a4 + 1, n):
                    k = (k4 * A[a5]) % p
                    if k == q:
                        ans += 1
print(ans)
