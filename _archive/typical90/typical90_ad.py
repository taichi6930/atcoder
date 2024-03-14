import collections
n, k = map(int, input().split())
A = [0] * (n + 1)

for i in range(2, n + 1):
    if A[i] == 0:
        for j in range(i, n + 1, i):
            A[j] += 1

c = collections.Counter(A)
ans = 0
for a in range(k, 9):
    ans += c[a]
print(ans)
