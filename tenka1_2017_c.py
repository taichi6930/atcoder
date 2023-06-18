N = int(input())
for h in range(3500, 0, -1):
    for n in range(3500, 0, -1):
        a = N * h * n
        b = 4 * n * h - N * n - N * h
        if b == 0:
            continue
        if a % b != 0:
            continue
        if a // b < n:
            continue
        exit(print(h, n, a // b))
