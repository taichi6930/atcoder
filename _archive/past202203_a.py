a, b, c = map(int, input().split())
ansList = [a * b, b * c, c * a]
print(min(ansList), max(ansList))
