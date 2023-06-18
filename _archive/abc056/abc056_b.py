w, a, b = map(int, input().split())
c = max(a, b) - min(a, b) - w
print(c if c > 0 else 0)
