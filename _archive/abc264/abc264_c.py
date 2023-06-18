import numpy as np
h1, w1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h1)]
nA = np.array(A)
h2, w2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(h2)]
nB = np.array(B)


def k(num):
    arr = []
    for i in range(2 ** num):
        arr_child = []
        for j in range(num):
            if i >> j & 1:
                arr_child.append(j)
        if len(arr_child) == 0:
            continue
        arr.append(arr_child)
    return arr


for a in k(h1):
    for b in k(w1):
        nC = np.copy(nA)
        print(nB)
        print(nC[a, b])
        print(a, b)

        print(np.allclose(nB, nC[a, b]))
