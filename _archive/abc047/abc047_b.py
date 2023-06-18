w, h, n = map(int, input().split())
sx, gx, sy, gy = 0, w, 0, h
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1 and sx < x:
        sx = x
    if a == 2 and gx > x:
        gx = x
    if a == 3 and sy < y:
        sy = y
    if a == 4 and gy > y:
        gy = y
if (gx-sx) > 0 and (gy-sy) > 0:
    print(max((gx-sx)*(gy-sy), 0))
else:
    print(0)
