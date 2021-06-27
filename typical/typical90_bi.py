q = int(input())
a = []

for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        a.insert(0, x)
        continue

    if t == 2:
        a.append(x)
        continue

    print(a[x - 1])
