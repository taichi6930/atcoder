n, y = map(int, input().split())

for a in range(y // 10000, -1, -1):
    for b in range((y - 10000 * a) // 5000, -1, -1):
        c = (y - a * 10000 - b * 5000) // 1000
        if a + b + c == n:
            exit(print(a, b, c))


print(-1, -1, -1)
