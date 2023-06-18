from bisect import bisect_left
n = int(input())
P = list(map(int, input().split()))
L = list(map(int, input().split()))
indexP = {p: i + 1 for i, p in enumerate(P)}
indexL = {l: i + 1 for i, l in enumerate(L)}
XY = [[] for _ in range(n)]

for i in range(1, n + 1):
    a = indexP[i]
    b = indexL[i]
    print(a, b)
