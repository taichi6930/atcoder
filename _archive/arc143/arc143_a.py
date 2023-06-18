a, b, c = map(int, input().split())
print(max(a, b, c) if (a + b + c - 2 * max(a, b, c)) >= 0 else -1)
