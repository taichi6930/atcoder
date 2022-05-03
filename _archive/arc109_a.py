a, b, x, y = map(int, input().split())
y = min(y, 2 * x)
a = a if a <= b else a - 1

print(x + y * abs(a - b))
