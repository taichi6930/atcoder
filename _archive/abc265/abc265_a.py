x, y, n = map(int, input().split())
print((n % 3) * x + min(3 * x, y) * (n - (n % 3)) // 3)
