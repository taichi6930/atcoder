d = int(input())
ans = d
for x in range(0, 10 ** 6 + 1):
    # 差が0になるようなyを求める
    y = (d - x ** 2) ** 0.5
    if y <= x:
        break
    intY = int(y)
    for y1 in range(intY -1 , intY + 2):
        ans = min(ans, abs(x ** 2 + y1 ** 2 - d))

print(ans)