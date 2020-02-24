a, b, k = map(int, input().split())
print(min(a - k, 0), min(
    b - k + a, 0))
