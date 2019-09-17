import fractions

n, X = map(int, input().split())
x = sorted(list(map(int, input().split())))

xXMin = abs(X - x[n-1])
xxMin = 10**10

if n != 1:
    for i in range(n-1):
        if xXMin > abs(X-x[i]):
            xXMin = abs(X-x[i])
        if xxMin > abs(x[i+1]-x[i]):
            xxMin = abs(x[i+1]-x[i])
    print(fractions.gcd(xXMin, xxMin))
else:
    print(abs(X - x[n-1]))
