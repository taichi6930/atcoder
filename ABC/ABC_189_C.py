n = int(input())
A = list(map(int, input().split()))
ans = 0

for l in range(n):
    for r in range(l + 1, n + 1):
        ans = max(min(A[l: r])*(r - l), ans)

print(ans)
