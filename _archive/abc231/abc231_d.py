from collections import *

n, m = map(int, input().split())
AB = [set() for _ in range(n)]
cAB = Counter()
for _ in range(m):
    a, b = map(int, input().split())
    AB[a - 1].add(b - 1)
    AB[b - 1].add(a - 1)
    cAB[a - 1] += 1
    cAB[b - 1] += 1

if m == 0:
    print('Yes')
    exit()

if cAB.most_common()[0][0] > 2:
    print('No')
    exit()

set1 = set()
set2 = set()

for key in list(cAB.keys()):
    if cAB[key] == 1:
        set1.add(key)
    if cAB[key] == 2:
        set2.add(key)

while len(set1) > 0:
    k = list(set1)[0]
    set1.discard(k)

    swi = True
    while swi:
        if cAB[k] == 0:
            print('No')
            exit()
        l = list(AB[k])[0]
        if cAB[k] == 1:
            swi = False
            set1.discard(l)
        cAB[k] -= 1
        cAB[l] -= 1
        AB[k].discard(l)
        AB[l].discard(k)
        set2.discard(k)
        set2.discard(l)
        if cAB[k] == 0:
            del cAB[k]
        if cAB[l] == 0:
            del cAB[l]

        l = k

print('Yes' if len(set2) == 0 else 'No')
