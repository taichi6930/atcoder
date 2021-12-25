n, k = map(int, input().split())
x = list(map(int, input().split()))
minX = abs(x[0]) * 2 + abs(x[len(x)-1])
for i in range(n-k+1):
    if x[i] * x[i+k-1] <= 0:
        minX = min(minX, min(abs(x[i]), abs(x[i+k-1]))
                   + abs(x[i]) + abs(x[i+k-1]))
    else:
        minX = min(minX, max(abs(x[i]), abs(x[i+k-1])))
print(minX)
