from bisect import bisect_left, bisect_right

n = int(input())
A = list(map(int, input().split()))
dicA = {}
setA = set()

for i, a in enumerate(A):
    if a not in setA:
        dicA[a] = []
    dicA[a].append(i + 1)
    setA.add(a)

q = int(input())
for _ in range(q):
    l, r, x = map(int, input().split())
    if x not in setA:
        print(0)
        continue
    lis = dicA[x]
    print(bisect_right(lis, r) - bisect_left(lis, l))
