w, h, x, y = map(int, input().split())
print(w * h / 2, 1 if (y / h == 0.5 and x / w == 0.5) else 0)
