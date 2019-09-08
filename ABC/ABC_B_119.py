n = int(input())
xSum = 0
for i in range(n):
    x, u = map(str, input().split())
    x = float(x)
    xSum += x if u == "JPY" else 380000 * x
print(xSum)
