n = int(input())
A = list(map(int, input().split()))
k = 0
l = 0

for i, a in enumerate(A):
    if a == i + 1:
        k += 1
        continue
    if A[A[i] - 1] == i + 1:
        l += 1

print((k * (k - 1) + l) // 2)
