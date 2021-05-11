m, h = map(int, input().split())
print("YNeos"[h % m > 0::2])
