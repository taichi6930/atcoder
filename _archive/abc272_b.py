from collections import Counter
n, m = map(int, input().split())
A = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    B = sorted(list(map(int, input().split()))[1:])
    lenB = len(B)
    for i in range(lenB - 1):
        for j in range(i + 1, lenB):
            A[B[i] - 1][B[j] - 1] = 1

for i in range(n - 1):
    for j in range(i + 1, n):
        if A[i][j] != 1:
            exit(print('No'))
print('Yes')
