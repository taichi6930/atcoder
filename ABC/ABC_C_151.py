n, m = map(int, input().split())
cntAC = 0
cntWA = 0
listAC = []
for i in range(m):
    p, s = map(str, input().split())
    if listAC.count(p) > 0:
        continue
    else:
        if s == "AC":
            cntAC += 1
            listAC.append(p)
        else:
            cntWA += 1

print(cntAC, cntWA)
