n, q = map(int, input().split())
TAB = [list(map(int, input().split())) for _ in range(q)]
fl = set()

for i, [t, a, b] in enumerate(TAB):
    ab_str = f'{a}-{b}'
    ba_str = f'{b}-{a}'
    if t == 1:
        fl.add(ab_str)
        continue
    if t == 2:
        if not ab_str in fl:
            continue
        fl.remove(ab_str)
        continue
    if t == 3:
        if not ab_str in fl or not ba_str in fl:
            print('No')
            continue
        print('Yes')
