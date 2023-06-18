n, p, q, r, s = map(int, input().split())
A = list(map(int, input().split()))
for i in range(-1, q - p):
    A[p + i], A[r + i] = A[r + i], A[p + i]

print(' '.join(list(map(lambda x: str(x), (A)))))
