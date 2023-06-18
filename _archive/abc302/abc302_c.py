n, m = map(int, input().split())
S = [input() for i in range(n)]
A = {k + 1: [] for k in range(n)}

for x in range(n - 1):
    for y in range(x + 1, n):
        cnt_x_y = 0
        for i in range(m):
            if S[x][i] != S[y][i]:
                cnt_x_y += 1
        if cnt_x_y == 1:
            A[x + 1].append(y + 1)
            A[y + 1].append(x + 1)
print(A)
