n, T = map(int, input().split())
cMin = 10000
for i in range(n):
    c, t = map(int, input().split())
    if cMin > c:
        cMin = min(c, cMin)
print(cMin if cMin != 10000 else "TLE")
