def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ansList = []

for h in range(H - 1):
    for w in range(W):
        if A[h][w] % 2 == 1:
            ansList.append(' '.join(int2strWithArray(
                [h + 1, w + 1, (h + 1) + 1, w + 1])))
            A[h][w] -= 1
            A[h + 1][w] += 1

for w in range(W - 1):
    if A[H - 1][w] % 2 == 1:
        ansList.append(' '.join(int2strWithArray(
            [H, w + 1, H, w + 2])))
        A[H - 1][w] -= 1
        A[H - 1][w + 1] += 1

print(len(ansList))
for ans in ansList:
    print(ans)
