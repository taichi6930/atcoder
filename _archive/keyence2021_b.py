from collections import Counter
n, k = map(int, input().split())
A = list(map(int, input().split()))
cA = Counter(A)
n = cA[0]
ans = 0

for i in range(10 ** 6):
    k = max(min(n, cA[i]) - min(n, cA[i + 1]), 0)
    ans += k * (i + 1)
    n = min(n, cA[i])
    if n == 0:
        break
print(ans)
