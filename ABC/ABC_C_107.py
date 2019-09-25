n, k = map(int, input().split())
x = list(map(int, input().split()))
y = [None] * (n-1)
for i in range(n-1):
    y[i] = x[i+1] - x[i]
print(y)
