n = int(input())
A = list(map(int, input().split()))

A1 = A[0: (2 ** n) // 2]
A2 = A[(2 ** n) // 2: (2 ** n)]
print(A.index(min(max(A1), max(A2))) + 1)
