n, K = map(int, input().split())
LRLis = ['A' for _ in range(n)]

for i in range(K):
    c, k = map(str, input().split())
    LRLis[int(k) - 1] = c

ans = 1

for i in range(n):
    if LRLis[i] != 'A':
        continue
    ans = (ans * (K - LRLis[:i].count('R') -
           LRLis[i + 1:].count('L'))) % 998244353

print(ans % 998244353)
