import numpy as np

H, W = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(H)])
Ah = [None] * H
Aw = [None] * W

for h in range(H):
    Ah[h] = sum(A[h, ])

for w in range(W):
    Aw[w] = sum(A[:, w])

print(Ah, Aw)
for h in range(H):
    k = [None] * W
    for w in range(W):
        k[w] = str(Ah[h] + Aw[w] - A[h, w])
    mojiretu = ' '.join(k)
    print(mojiretu)
