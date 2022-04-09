n = int(input())
T = list(input())

x, y = 0, 0
swi = 0

tList = [[1, 0], [0, -1], [-1, 0], [0, 1]]

for t in T:
    if t == 'R':
        swi = (swi + 1) % 4
        continue
    tl = tList[swi]
    x += tl[0]
    y += tl[1]

print(x, y)
