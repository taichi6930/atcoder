H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        p = C[h][w]

        if p != '.':
            continue

        checkList = [False] * 5

        for [x, y] in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            if 0 <= w + x < W and 0 <= h + y < H:
                q = C[h + y][w + x]
                if q == '.':
                    continue
                checkList[int(q) - 1] = True

        for i, cl in enumerate(checkList):
            if not(cl):
                C[h][w] = str(i + 1)
                break

for i in range(H):
    print(''.join(C[i]))
