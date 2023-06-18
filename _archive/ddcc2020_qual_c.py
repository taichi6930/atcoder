h, w, k = map(int, input().split())
S = [list(input()) for _ in range(h)]
A = [[0 for _ in range(w)] for _ in range(h)]

num = -1

for i in range(h):
    swi = False
    for j in range(w):
        if j == 0:
            