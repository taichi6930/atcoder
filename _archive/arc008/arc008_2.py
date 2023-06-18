from collections import Counter
from math import ceil

n, m = map(int, input().split())
cName = Counter(list(input()))
cKit = Counter(list(input()))

ans = 0

for key in list(cName.keys()):
    if cKit[key] == 0:
        ans = -1
        break
    ans = max(ceil((cName[key]) / cKit[key]), ans)

print(ans)
