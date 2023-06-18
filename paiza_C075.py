n, m = map(int, input().split())
F = [int(input()) for _ in range(m)]
p = 0

for f in F:
    if p >= f:
        p -= f
    elif p < f:
        n -= f
        p += f // 10
    print(n, p)
