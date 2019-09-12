n, m = map(int, input().split())
lMax = 0
rMin = n
for i in range(m):
    l, r = map(int, input().split())
    lMax = max(l, lMax)
    rMin = min(r, rMin)
print(rMin - lMax + 1 if rMin >= lMax else 0)
