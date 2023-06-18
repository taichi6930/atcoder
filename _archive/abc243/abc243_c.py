n = int(input())
XY = [list(map(int, input().split())) for _ in range(n)]
S = list(input())
dicL = {}
dicR = {}
setL = set()
setR = set()
ans = 'No'

for i in range(n):
    y, x = XY[i][1], XY[i][0]

    if S[i] == 'L':
        if y not in dicL:
            dicL[y] = x
        else:
            dicL[y] = max(x, dicL[y])
        setL.add(y)
        if y in setR:
            if dicR[y] < dicL[y]:
                ans = 'Yes'
    if S[i] == 'R':
        if y not in dicR:
            dicR[y] = x
        else:
            dicR[y] = min(x, dicR[y])
        setR.add(y)
        if y in setL:
            if dicR[y] < dicL[y]:
                ans = 'Yes'

print(ans)
