def main():
    n = int(input())
    ansX, ansY = -1, -1

    X, Y = [0] * n, [0] * n
    for i in range(n):
        X[i], Y[i] = map(int, input().split())
    X.sort()
    Y.sort()

    x, y = sum(X) / n, sum(Y) / n

    anskX = 0
    for i in range(n):
        anskX += abs(x - X[i])
    if ansX < 0:
        ansX = anskX
    else:
        ansX = min(ansX, anskX)

    anskY = 0
    for i in range(n):
        anskY += abs(y - Y[i])
    if ansY < 0:
        ansY = anskY
    else:
        ansY = min(ansY, anskY)

    print(ansX + ansY, x, y)


if __name__ == '__main__':
    main()
