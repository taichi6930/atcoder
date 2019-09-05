m, q = map(int, input().split())
n = [0] * m
# n[2:4] = 1
for i in range(q):
    l, r, t = map(int, input().split())
    for j in range(l-1, r):
        n[j] = t

for i in range(m):
    print(n[i])
