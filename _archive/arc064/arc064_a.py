n, x = map(int, input().split())
A = list(map(int, input().split()))
B = [A[i] + A[i + 1] for i in range(n - 1)]

ans = 0

for i in range(len(B)):
    k = max(0, B[i] - x)
    ans += k
    B[i] -= k
    if i >= n - 2:
        break
    B[i + 1] -= k

print(ans)
