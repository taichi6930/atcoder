a, b, c = map(int, input().split())
setA = set()
for i in range(1, 10 ** 9):
    q = (a * i) % b
    if q == c:
        exit(print('YES'))
    if q in setA:
        exit(print('NO'))
    setA.add(q)
