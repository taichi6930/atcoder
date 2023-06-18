xlis = set()
ylis = set()

for i in range(3):
    x, y = map(int, input().split())
    if x in xlis:
        xlis.discard(x)
    else:
        xlis.add(x)
    if y in ylis:
        ylis.discard(y)
    else:
        ylis.add(y)

print(list(xlis)[0], list(ylis)[0])
