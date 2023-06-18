n, k = map(int, input().split())
A = list(map(int, input().split()))
B = []
setA = set(A)

for i in range(n):
    if i + 1 in setA:
        continue
    B.append(i + 1)

XY = [list(map(int, input().split())) for _ in range(n)]

rmax = 0
for b in B:
    r = 1000000000000
    for a in A:
        rr = ((XY[a - 1][0] - XY[b - 1][0]) ** 2 +
              (XY[a - 1][1] - XY[b - 1][1]) ** 2) ** 0.5
        r = min(r, rr)
    rmax = max(rmax, r)

print(rmax)
