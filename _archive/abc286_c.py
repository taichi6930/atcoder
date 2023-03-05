n, a, b = map(int, input().split())
S = input()

ans = b * n

for i in range(n):
    T = S[i:] + S[:i]
    cnt = a * i
    for j in range((n + 1) // 2):
        if T[j] != T[n - j - 1]:
            cnt += b
    ans = min(ans, cnt)
print(ans)
