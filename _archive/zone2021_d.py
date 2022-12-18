from collections import *
S = list(input())
T = deque()

swi = True

for s in S:
    if s == 'R':
        swi = not(swi)
        continue
    T.append(s) if swi else T.appendleft(s)

U = []

for i, t in enumerate((T if swi else list(T)[::-1])):
    if len(U) == 0:
        U.append(t)
        continue
    if t == U[-1]:
        U.pop()
        continue
    U.append(t)

print(''.join(U))
