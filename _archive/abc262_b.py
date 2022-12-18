from collections import Counter
n, m = map(int, input().split())
UV = {i + 1: [] for i in range(n)}
for i in range(m):
    u, v = map(int, input().split())
    UV[min(u, v)].append(max(u, v))

ans = 0

for a in range(n):
    lenlis = len(UV[a + 1])
    if lenlis < 2:
        continue
    lis = sorted(UV[a + 1])

    for b in range(lenlis - 1):
        for c in range(b + 1, lenlis):
            if lis[c] in UV[lis[b]]:
                ans += 1

print(ans)
