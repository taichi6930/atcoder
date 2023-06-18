n = int(input())
A = [list(input()) for _ in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        if A[i][j] == A[j][i]:
            if A[i][j] == 'D':
                continue
            exit(print('incorrect'))
        if A[i][j] == 'W' and A[j][i] == 'L':
            continue
        if A[i][j] == 'L' and A[j][i] == 'W':
            continue
        exit(print('incorrect'))

print('correct')
