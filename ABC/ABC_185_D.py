import math
n, m = map(int, input().split())
Alist = [0] + sorted(list(map(int, input().split()))) + [n + 1]
if n == m:
    print(0)
    exit()
if m == 0:
    print(1)
    exit()
maxN = 10 ** 9
for i in range(len(Alist)-1):
    if Alist[i + 1] - Alist[i] == 1:
        continue
    if Alist[i + 1] - 1 - Alist[i] < maxN:
        maxN = Alist[i + 1] - 1 - Alist[i]
Alist2 = [0] * (m + 1)
for i in range(len(Alist2)):
    Alist2[i] = max(0, math.ceil((Alist[i + 1] - Alist[i] - 1) / maxN))
print(sum(Alist2))
