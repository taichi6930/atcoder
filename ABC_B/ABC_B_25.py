n, a, b = map(int, input().split())
for i in range(n):
    s, d = map(str, input().split())
    sign = (-1 if s == "West" else 1)
