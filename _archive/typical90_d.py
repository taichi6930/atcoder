h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
row = [0] * h
column = [0] * w

for i in range(h):
    for j in range(w):
        row[i] += A[i][j]
        column[j] += A[i][j]

for i in range(h):
    print(*[row[i] + column[j] - A[i][j] for j in range(w)])
