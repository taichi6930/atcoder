def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


h, w = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))

C = [[0 for _ in range(w)] for _ in range(h)]

cnt = 0
for i in range(h * w):
    if cnt == h * w:
        break
    for k in range(A[i]):
        if cnt == h * w:
            break
        C[cnt // w][cnt % w] = i + 1
        cnt += 1

for i, c in enumerate(C):
    print(' '.join(int2strWithArray(c[::(-1) ** i])))
