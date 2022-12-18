from pprint import *
n = int(input())
A = [[0 for _ in range(12)] for _ in range(12)]
for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    for a1 in range(ly, ry + 1):
        A[lx][a1] += 1
    for a2 in range(ly, ry + 1):
        A[rx][a2] -= 1
    for a3 in range(lx + 1, rx + 1):
        A[a3][ly] += 1
    for a4 in range(lx + 1, rx):
        A[a4][ry] -= 1

pprint(A)
