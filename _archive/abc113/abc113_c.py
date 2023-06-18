n, m = map(int, input().split())
pyDic = {}
pyArray = [None] * m
for i in range(m):
    p, y = map(int, input().split())
    pyArray[i] = [p, y]
    if str(p) in pyDic:
        pyDic[str(p)].append(y)
        pyDic[str(p)].sort()
    else:
        pyDic[str(p)] = [y]

for i in range(m):
    print('{:06}'.format(
        pyArray[i][0]) + '{:06}'.format(pyDic[str(pyArray[i][0])].index(pyArray[i][1]) + 1))
