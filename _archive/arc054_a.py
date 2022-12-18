l, x, y, s, d = map(int, input().split())
D = sorted([d, d + l if s - d > 0 else d - l])
k1 = (max(D) - s) / (x + y)
k2 = (s - min(D)) / (y - x) if y - x != 0 else 10 ** 9

print(k1 if x >= y else min(k1, k2))
