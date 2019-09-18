import fractions

n, X = map(int, input().split())
x = sorted(list(map(int, input().split())))

xxMin = 10**10

for i in range(n-1):
    if xxMin > abs(x[i+1]-x[i]):
        xxMin = abs(x[i+1]-x[i])
else:
    print(abs(X - x[n - 1]))

print
xXMin = abs(X - x[n - 1])
    if xXMin > abs(X-x[i]):
        xXMin = abs(X-x[i])
