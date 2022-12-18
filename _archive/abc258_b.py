n = int(input())
A = [list(input()) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(n):
        si, sj = i, j
        for _, [dx, dy] in enumerate([[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]):
            num = ''
            for k in range(n):
                num += A[(si + dx * k) % n][(sj + dy * k) % n]
            ans = max(ans, int(num))

print(ans)
