h, m = map(int, input().split())

for i in range(10 ** 10):

    h1 = (h // 10) * 10 + m // 10
    m1 = (h % 10) * 10 + m % 10

    if 0 <= h1 < 24 and 0 <= m1 < 60:
        exit(print(h, m))
    m += 1
    if m >= 60:
        h = (h + 1) % 24
        m = m % 60
