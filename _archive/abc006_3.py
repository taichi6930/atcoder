n, m = map(int, input().split())

for a in range(10 ** 5 + 1):
    b = 4 * n - m - 2 * a
    c = m - 3 * n + a
    if b >= 0 and c >= 0:
        print(a, b, c)
        exit()

print(-1, -1, -1)
