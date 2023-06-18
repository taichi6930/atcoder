from collections import Counter
n, k = map(int, input().split())
c = Counter()

for i in range(n):
    a, b = map(int, input().split())
    c[a] += b

sumC = 0
for key in sorted(list(c.keys())):
    sumC += c[key]
    if sumC >= k:
        exit(print(key))
