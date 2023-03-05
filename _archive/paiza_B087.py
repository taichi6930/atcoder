h, w, k = map(int, input().split())
S = [input() for _ in range(h)]
S2 = ['' for _ in range(w)]
for i, s in enumerate(S):
    for j in range(w):
        S2[j] += s[j]

ans = 0

for s in S:
    for i in range(h - k + 1):
        ans = max(ans, int(s[i: i + k]))

for s2 in S2:
    for i in range(w - k + 1):
        ans = max(ans, int(s2[i: i + k]))

print(ans)
