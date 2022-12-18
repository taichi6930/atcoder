from collections import *
q = int(input())
K = deque([])
op = []
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        K.appendleft(x)
    if t == 2:
        K.append(x)
    if t == 3:
        op.append(K[x - 1])

print(*op, sep='\n')
