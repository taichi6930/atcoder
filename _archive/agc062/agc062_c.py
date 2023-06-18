n, k = map(int, input().split())
A = [2**i for i in range(n)]
# A = sorted(list(map(int, input().split())))
B = set()
for i, a in enumerate(A):
    old_b = set() | B
    B.add(a)
    for b in old_b:
        B.add(b + a)
print(len(B))
