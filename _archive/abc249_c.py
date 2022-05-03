from collections import Counter
n, k = map(int, input().split())
S = [list(input()) for _ in range(n)]
ans = 0

for i in range(2 ** n):
    lis = []
    for j, s in enumerate(S):
        if (i >> j & 1):
            lis += s
    cLis = Counter(lis)
    cnt = 0
    for key in cLis.keys():
        if cLis[key] == k:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
