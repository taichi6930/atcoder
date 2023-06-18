n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
ans = abs(A[0] - B[0])
a = 0
b = 0

for i in range(n + m):
    if a >= n or b >= m:
        break
    ans = min(ans, abs(A[a] - B[b]))
    if A[a] >= B[b]:
        b += 1
        continue
    a += 1

print(ans)
