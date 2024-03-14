n = int(input())
X = []
Y = []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()

ansX, ansY = 10 ** 15, 10 ** 15

xpList = [X[(len(X) - 1) // 2]] if len(X) % n == 1 else [
    X[(len(X)) // 2], X[(len(X) - 1) // 2]]
ypList = [Y[(len(Y) - 1) // 2]] if len(Y) % n == 1 else [
    Y[(len(Y)) // 2], Y[(len(Y) - 1) // 2]]

for xp in xpList:
    k = 0
    for x in X:
        k += abs(x - xp)
    ansX = min(ansX, k)

for yp in ypList:
    k = 0
    for y in Y:
        k += abs(y - yp)
    ansY = min(ansY, k)


print(ansX + ansY)
