H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for h in range(H):
    for w in range(W):
        A[h][w] = chr(A[h][w] + 64) if A[h][w] > 0 else '.'
    print(''.join(A[h]))
