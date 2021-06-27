n, q = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for i in range(q):
    t, x, y = map(int, input().split())

    xa = (- cnt + x - 1) % n
    ya = (- cnt + y - 1) % n

    if t == 1:
        a[xa], a[ya] = a[ya], a[xa]
        continue

    if t == 2:
        cnt = (cnt + 1) % n
        continue

    if t == 3:
        print(a[xa])
