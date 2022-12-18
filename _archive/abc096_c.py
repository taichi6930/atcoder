h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            continue
        if i - 1 >= 0:
            if S[i - 1][j] == "#":
                continue
        if j - 1 >= 0:
            if S[i][j - 1] == "#":
                continue
        if i + 1 < h:
            if S[i + 1][j] == "#":
                continue
        if j + 1 < w:
            if S[i][j + 1] == "#":
                continue
        exit(print('No'))

print('Yes')
