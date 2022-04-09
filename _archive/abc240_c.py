n, x = map(int, input().split())
minAB = 0
AB = set()
for i in range(n):
    a, b = map(int, input().split())
    newAB = set()
    if len(AB) == 0:
        AB.add(a)
        AB.add(b)
        continue
    for ab in list(AB):
        if a + ab <= x:
            newAB.add(a + ab)
        if b + ab <= x:
            newAB.add(b + ab)
    AB = newAB

if x in AB:
    print('Yes')
else:
    print('No')
