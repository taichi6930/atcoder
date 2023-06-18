n, p = map(int, input().split())
ans = 0

for a1 in range(n):
    for a2 in range(n // 2):
        if a1 + a2 * 2 > n:
            break
        # print(a1, a2, n - (a1 + a2 * 2))
print(ans)
print(a1, a2, n - (a1 + a2 * 2))
