from collections import defaultdict
n = int(input())
setA = set()
lis = defaultdict(list)
maxA = 1

for i in range(n):
    a, b = map(int, input().split())
    lis[a].append(b)
    lis[b].append(a)


def f(k):
    global maxA
    if k in setA:
        return
    maxA = max(k, maxA)
    setA.add(k)
    for i in lis[k]:
        f(i)


f(1)

print(maxA)
