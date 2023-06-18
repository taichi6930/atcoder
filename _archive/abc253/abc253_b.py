h, w = map(int, input().split())
oList = []

for i in range(h):
    s = list(input())
    for j in range(w):
        if s[j] == 'o':
            oList.append([j, i])

print(abs(oList[0][0] - oList[1][0]) + abs(oList[0][1] - oList[1][1]))
