from collections import defaultdict

n = int(input())
P = list(map(int, input().split()))

d = defaultdict(int)
for i, p in enumerate(P):
    d[p] = i
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    print(a if d[a] <= d[b] else b)
