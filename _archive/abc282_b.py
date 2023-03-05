n, m = map(int, input().split())
S = [int(input().replace('o', '1').replace('x', '0'), 2) for _ in range(n)]
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if S[i] | S[j] == 2 ** m - 1:
            ans += 1

print(ans)
