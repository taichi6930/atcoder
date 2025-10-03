from collections import Counter

n, t = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(t)]
listAB = [0 for _ in range(n)]


c = Counter({0: n})
cnt = 1

for i, [a, b] in enumerate(AB):
    beforeNum = listAB[a - 1]
    afterNum = b + beforeNum

    listAB[a - 1] += b

    if c[beforeNum] == 1:
        cnt -= 1
    c[beforeNum] -= 1

    if c[afterNum] == 0:
        cnt += 1
    c[afterNum] += 1

    print(cnt)
