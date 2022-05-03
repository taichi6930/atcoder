h, w = map(int, input().split())

C = [list(input())for _ in range(h)]

points = ["0-0"]
ans = 1

for i in range(1, 10000):
    newPoints = []
    for point in points:
        x, y = map(int, point.split("-"))
        if x + 1 < w:
            if C[y][x + 1] == ".":
                newPoints.append(str(x + 1) + "-" + str(y))
                ans = y + x + 2

        if y + 1 < h:
            if C[y + 1][x] == ".":
                newPoints.append(str(x) + "-" + str(y + 1))
                ans = y + x + 2
    points = list(set(newPoints))
    if len(points) == 0:
        break

print(ans)
