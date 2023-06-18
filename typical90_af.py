n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

Q = [[] for _ in range(n)]

m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    Q[x - 1].append(y)
    Q[y - 1].append(x)

ans = 1000 ** 2
swi = False

numList = [p + 1 for p in range(n)]


def depth(nowList, k, cnt):
    global n, ans, numList, swi
    k += A[nowList[-1] - 1][cnt]
    cnt += 1
    if len(nowList) == n:
        ans = min(ans, k)
        swi = True
        return

    for num in numList:
        if num in nowList:
            continue
        if nowList[-1] in Q[num - 1]:
            continue
        depth(nowList + [num], k, cnt)


for num in numList:
    depth([num], 0, 0)

print(ans if swi else -1)
