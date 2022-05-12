from collections import deque
n, m = map(int, input().split())
ansList = deque([])
kList = deque([])


AB = sorted([list(map(int, input().split()))
            for _ in range(m)], key=lambda x: (x[1], x[0]))

for i, [a, b] in enumerate(AB):
    swi = True
    for j in range(len(kList)):
        [ks, kg] = kList[0]
        if kg < a + 0.5:
            w = kList.popleft()
            ansList.append(w)
            continue
        kList.popleft()
        kList.append([max(a + 0.5, ks), min(b - 0.5, kg)])
        swi = False

    if swi:
        kList.append([a, b])


print(len(list(ansList)) + len(list(kList)))
