n, m, q = map(int, input().split())
A, B, C, D = [0] * q, [0] * q, [0] * q, [0] * q

for i in range(q):
    a, b, c, d = map(int, input().split())
    A[i], B[i], C[i], D[i] = a, b, c, d

print(A)
