for _ in range(10 ** 9):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    c = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for i in range(w)]for j in range(h)]

    cnt = 0
    xy_move = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            xy_move.append([i, j])

    for i in range(w):
        for j in range(h):
            if visited[j][i] == 1 or c[j][i] == 0:
                continue

            stack = [[i, j]]
            cnt += 1

            while stack:
                x, y = stack.pop()
                c[y][x] = 0

                for k in xy_move:
                    x_move, y_move = k
                    nx = x + x_move
                    ny = y + y_move

                    if 0 <= nx < w and 0 <= ny < h and c[ny][nx] == 1 and visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        c[ny][nx] = 0
                        stack.append([nx, ny])

    print(cnt)
