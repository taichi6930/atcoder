a, b, c, k = map(int, input().split())
print(max(min(a, k), 0) - max(min(c, k - a - b), 0))
