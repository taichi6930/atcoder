import math

n = int(input())
k = math.ceil((-1 + (1 + 8 * n) ** 0.5) / 2)
ans = []
for i in range(k):
    if n - k + i < 0:
        if n != 0:
            ans.append(n)
        break
    ans.append(k - i)
    n -= k - i

for a in ans:
    print(a)
