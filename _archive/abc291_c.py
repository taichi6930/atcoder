n = int(input())
s = input()

# 初期座標は原点 (0, 0)
x = 0
y = 0

# すでに訪れた座標を記録するためのset
visited = set([(0, 0)])

# N回の移動を順番に実行し、訪れた座標をvisitedに追加していく
for i in range(n):
    if s[i] == 'R':
        x += 1
    elif s[i] == 'L':
        x -= 1
    elif s[i] == 'U':
        y += 1
    elif s[i] == 'D':
        y -= 1

    if (x, y) in visited:
        print("Yes")
        exit()

    visited.add((x, y))

print("No")
