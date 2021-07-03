h, n = map(int, input().split())
aListSum = sum(list(map(int, input().split())))
print("YNeos"[h - aListSum > 0::2])
