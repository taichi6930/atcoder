n, k, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for i in range(n):
    q = A[i] // x
    if k < q:
        q = k
    k -= q
    A[i] -= x * q

A = sorted(A, reverse=True)

for j in range(min(n, k)):
    A[j] = 0

print(sum(A))
