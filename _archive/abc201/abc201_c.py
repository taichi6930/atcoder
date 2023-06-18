oList = []
nList = []
ans = 0

s = list(input())
for i in range(10):
    if s[i] == 'o':
        oList.append(str(i))
        continue
    if s[i] == 'x':
        nList.append(str(i))
        continue

for i in range(10000):
    n = list(format(i, '0>4'))
    ansi = 1

    for a in range(len(oList)):
        if n.count(oList[a]) <= 0:
            ansi = 0
            break

    for b in range(len(nList)):
        if n.count(nList[b]) > 0:
            ansi = 0
            break

    ans += ansi

print(ans)
