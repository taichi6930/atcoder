x, y, z = map(int, input().split())
if x < 0:
    x = - x
    y = - y
    z = - z

if y < 0 or x < y:
    exit(print(x))

if z < y and y < x:
    exit(print(x + 2 * abs(min(z, 0))))
print(-1)
