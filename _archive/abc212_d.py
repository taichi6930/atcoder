from collections import defaultdict
q = int(input())
d = defaultdict(int)
numD = 0

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 3:
        continue
    x = query[1]
    if query[0] == 1:
        d[x] += 1
        numD += 1
        continue
    if query[0] == 2:
        d = defaultdict(int)
        d[x] += numD

print(d)
