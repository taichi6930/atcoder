lis = [[0 for _ in range(9)] for _ in range(9)]
a, b = map(int, input().split())
sList = []

for i in range(3):
    S = list(input())
    for j, s in enumerate(S):
        if s == '#':
            sList.append([i - 1, j - 1])


def f(nowX, nowY):
    global cnt
    cnt += 1
    if lis[nowX][nowY] == 1:
        return
    lis[nowX][nowY] = 1
    for (x, y) in sList:
        newX = x + nowX
        newY = y + nowY
        if 0 <= newX < 9 and 0 <= newY < 9:
            f(newX, newY)


f(a - 1, b - 1)

print(sum([sum(li) for li in lis]))
