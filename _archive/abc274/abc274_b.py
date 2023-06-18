h, w = map(int, input().split())
C = [list(input()) for _ in range(h)]

ans = [0] * w

for i, c in enumerate(C):
    for j in range(w):
        if c[j] == '#':
            ans[j] += 1

print(*ans)
