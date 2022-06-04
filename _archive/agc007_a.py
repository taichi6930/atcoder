from copy import deepcopy
h, w = map(int, input().split())
A = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    a = list(input())
    for j in range(w):
        if a[j] == '#':
            A[i][j] = 1


def f():
    swi = False
    for [dx, dy] in enumerate([[1, 0], [0, 1]]):
        newX = x + dx
        newY = y + dy
        if newX >= w or newY >= h:
            continue
        swi = True
        


print(A)
