n, x = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(n)], reverse=True)

ABset = set([0])

for i, [a, b] in enumerate(AB):
    temp_ABset = set()
    for j in range(b + 1):
        for k in ABset:
            if j * a + k > x:
                continue
            if j * a + k == x:
                exit(print('Yes'))
            temp_ABset.add(j * a + k)
    ABset.update(temp_ABset)

exit(print('No'))
