from copy import deepcopy
H, W = map(int, input().split())
A = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    a = list(input())
    for j in range(W):
        if a[j] == '#':
            A[i][j] = 1


key = 100
keyNum = []
for h in range(H):
    for w in range(W):
        if A[h][w] == 0:
            continue
        if h + w >= key:
            continue
        keyNum = [h, w]
        key = h + w

if key == 100:
    print('Possible')
    exit()


def f(x, y, oldA, k):
    swi = False
    for _, [dx, dy] in enumerate([[1, 0], [0, 1]]):
        newX = x + dx
        newY = y + dy
        if newX > w or newY > h:
            if sum([sum(a) for a in oldA]) == 0:
                print('Possible')
                exit()
            continue
        if oldA[newY][newX] == 0:
            continue
        swi = True
        newA = deepcopy(oldA)
        newA[newY][newX] = 0
        f(newX, newY, newA, k)
    if not(swi):
        if sum([sum(a) for a in oldA]) == 0:
            print('Possible')
            exit()


A[keyNum[1]][keyNum[0]] = 0
f(keyNum[1], keyNum[0], deepcopy(A), 0)

print('Impossible')
