n, k = map(int, input().split())
A = list(map(int, input().split()))

B = [0] + [0] * n
ans = 0
for i in range(n):
    B[i + 1] = B[i] + A[i]

for x in range(n):
    for y in range(x, n):
        if B[y + 1] - B[x] >= k:
            ans += 1

print(ans)
