n, m, x, t, d = map(int, input().split())
k = x - m
print(t if x <= m else t - k * d)
