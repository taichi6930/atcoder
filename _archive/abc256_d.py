from collections import *
n = int(input())
lr = {}
rSet = set()
for _ in range(n):
    l, r = map(int, input().split())
    lr[l] = max(r, lr[l]) if l in lr else r

swi = False
s, g = 0, 0
lrKeys = sorted(list(lr.keys()))

for key in lrKeys:
    if not(swi):
        swi = True
        s = key
        g = lr[key]
    if s <= key and key <= g:
        g = max(g, lr[key])
    else:
        print(s, g)
        s = key
        g = lr[key]

print(s, g)
