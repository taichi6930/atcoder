from copy import deepcopy
from pprint import *
n, m, q = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(q)]
A = [None for _ in range(n)]
ABList = [[[0, 0, 0]] for _ in range(q)]

for i, (a, b, c, d) in enumerate(ABCD):
    for j in range(m):
        if m - j - c <= 0:
            break
        ABList[i].append([d, m - j, m - j - c])

ans = 0


def f(num, oldA, score):
    global ans
    if num == q:
        newA = [m + 1] + deepcopy(oldA)
        for p in range(n):
            if newA[p + 1] is None:
                newA[p + 1] = newA[p]
                continue
            if newA[p + 1] > newA[p]:
                return
        ans = max(ans, score)
        return
    (a, b, _, _) = ABCD[num]
    for j, (scr, aNum, bNum) in enumerate(ABList[num]):
        newA = deepcopy(oldA)
        if scr == 0:
            f(num + 1, newA, score)
            continue
        if newA[a - 1] is not None and newA[a - 1] != aNum:
            continue
        newA[a - 1] = aNum
        if newA[b - 1] is not None and newA[b - 1] != bNum:
            continue
        newA[b - 1] = bNum
        f(num + 1, newA, score + scr)


f(0, A, 0)
print(ans)
