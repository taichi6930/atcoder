n, q = map(int, input().split())
A = list(map(int, input().split()))
B = [A[i + 1] - A[i] for i in range(n - 1)]

ans = sum([abs(B[i]) for i in range(n - 1)])

for _ in range(q):
    l, r, v = map(int, input().split())
    if l > 1:
        ans -= abs(B[l - 2])
        B[l - 2] += v
        ans += abs(B[l - 2])
    if r < n:
        ans -= abs(B[r - 1])
        B[r - 1] -= v
        ans += abs(B[r - 1])
    print(ans)
