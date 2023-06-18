n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(m)]
B = {i + 1: set(j + 1 for j in range(i + 1, n)) for i in range(n - 1)}
for i, a in enumerate(A):
    for j in range(n - 1):
        mi, ma = sorted(a[j : j + 2])
        B[mi].discard(ma)

print(sum([len(b) for b in B.values()]))
