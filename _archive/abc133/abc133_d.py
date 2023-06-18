n = int(input())
A = list(map(int, input().split()))

sumA = sum([A[i] * (-1) ** i for i in range(n)])

B = [str(sumA)] + [None] * (n - 1)

for i in range(1, n):
    sumA = - 1 * (sumA - A[i - 1]) + A[i - 1]
    B[i] = str(sumA)

print(' '.join(B))
