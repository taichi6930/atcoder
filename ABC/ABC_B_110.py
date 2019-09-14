n, m, x, y = map(int, input().split())
xMax = max(map(int, input().split()))
yMin = min(map(int, input().split()))
swi = "No War"

if yMin < xMax+1:
    swi = "War"
else:
    for i in range(xMax+1, yMin+1):
        if not(x+1 <= i <= y):
            swi = "War"
            break
print(swi)
