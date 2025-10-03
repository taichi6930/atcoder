S = input()
ans = 0

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        s = S[i:j]
        if len(s) < ans:
            continue
        if s == s[::-1]:
            ans = max(ans, len(s))
print(ans)
