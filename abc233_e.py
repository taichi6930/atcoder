def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


X = str2intWithArray(list(input()))[::-1]
sumX = sum(X)

xBox = [0] * (10 ** 6)

for i, x in enumerate(xBox):
    xBox[i] = sumX
    sumX -= X[i]
    if sumX <= 0:
        break


for i in range(10 ** 6):
    kList = str2intWithArray(list(str(xBox[i]))[::-1])
    xBox[i] = 0
    for j, k in enumerate(kList):
        xBox[i + j] += k

for i in range(10 ** 6):
    if xBox[-1] != 0:
        break
    xBox.pop()
print(''.join(int2strWithArray(xBox)[::-1]))
