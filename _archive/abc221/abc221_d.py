n = int(input())
X = {}
D = [0 for _ in range(n)]


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


for i in range(n):
    a, b = map(int, input().split())
    if not a in X:
        X[a] = 0
    X[a] += 1
    if X[a] == 0:
        X.pop(a)
    if not a + b in X:
        X[a + b] = 0
    X[a + b] -= 1
    if X[a + b] == 0:
        X.pop(a + b)

xKeys = sorted(list(X.keys()))

y = X[xKeys[0]]

for i in range(len(xKeys) - 1):
    if y - 1 >= 0:
        D[y - 1] += xKeys[i + 1] - xKeys[i]
    y += X[xKeys[i + 1]]

print(' '.join(int2strWithArray(D)))
