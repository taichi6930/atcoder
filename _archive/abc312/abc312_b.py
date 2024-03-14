n, m = map(int, input().split())
S = [list(input()) for _ in range(n)]


def ck(i, j):
    for _i in range(0, 3):
        for _j in range(0, 3):
            if S[i + _i][j + _j] != "#":
                return False
    for _i in range(6, 9):
        for _j in range(6, 9):
            if S[i + _i][j + _j] != "#":
                return False
    for _i in range(0, 4):
        if S[i + _i][j + 3] != ".":
            return False
    for _j in range(0, 4):
        if S[i + 3][j + _j] != ".":
            return False
    for _i in range(5, 9):
        if S[i + _i][j + 5] != ".":
            return False
    for _j in range(5, 9):
        if S[i + 5][j + _j] != ".":
            return False
    return True


for i in range(n - 8):
    for j in range(m - 8):
        if ck(i, j):
            print(i + 1, j + 1)
