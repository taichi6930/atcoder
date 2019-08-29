a, b = map(int, input().split())
print(max(a, b) * 2 - 1 if abs(a - b) >= 2 else a + b)
