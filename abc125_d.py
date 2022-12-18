n = int(input())
A = list(map(int, input().split()))

for i in range(n - 1):
    if A[i] > 0:
        continue
    if A[i] + A[i + 1] > 0:
        continue
    A[i] = - A[i]
    A[i + 1] = - A[i + 1]

print(sum(A))
