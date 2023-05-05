n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
maxAB = max(max(A), max(B))
A.append(maxAB + 1)
B.append(maxAB + 1)
Alis, Blis = [], []

i, j = 0, 0
for k in range(n + m):
    if A[i] < B[j]:
        Alis.append(k + 1)
        i += 1
        continue
    Blis.append(k + 1)
    j += 1

print(*Alis)
print(*Blis)
