n = int(input())
A = list(map(int, input().split()))
B = set([i + 1 for i in range(n)])

for i, a in enumerate(A):
    if i + 1 not in B:
        continue
    B.discard(a)
print(len(B))
print(*list(B))
