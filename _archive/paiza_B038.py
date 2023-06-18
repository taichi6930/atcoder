a, b, c, d = map(int, input().split())

if (c + d) * b == a * 2 and b % 2 == 0:
    exit(print(1, 1))

if (c - d) == 0:
    exit(print('miss'))

if (a - b * d) % (c - d) != 0:
    exit(print('miss'))

if (a - b * c) % (d - c) != 0:
    exit(print('miss'))

x = (a - b * d) // (c - d)
y = (a - b * c) // (d - c)

if x <= 0 or y <= 0:
    exit(print('miss'))

print(x, y)
