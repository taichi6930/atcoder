n = int(input())
A = list(map(int, input().split()))

A2sum = sum(A) ** 2
for i in range(n):
    A2sum -= (A[i] ** 2)

print((A2sum // 2) % (10 ** 9 + 7))
