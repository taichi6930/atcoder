from math import ceil
from bisect import bisect_right

m = 1000000

primeTF = [False, False] + [True] * (m - 2)
n = int(input())
ans = 0

primeList = []
for i in range(m):
    if primeTF[i]:
        primeList.append(i)
        for j in range(m):
            if i * (j + 2) >= m:
                break
            primeTF[i * (j + 2)] = False

for i, q in enumerate(primeList):
    if 2 * q ** 3 > n:
        break
    bpp = bisect_right(primeList, int(min(n / (q ** 3), q) + 1) + 1)
    for j in range(n):
        k = bpp - j
        if k < 0:
            break
        if primeList[k] >= q:
            continue
        if primeList[k] * (q ** 3) <= n:
            ans += k + 1
            break

print(ans)
