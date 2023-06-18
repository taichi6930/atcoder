h, w = map(int, input().split())

S = [[] for _ in range(w)]
T = [[] for _ in range(w)]

for _ in range(h):
    for i, l in enumerate(list(input())):
        S[i].append(l)

for _ in range(h):
    for i, l in enumerate(list(input())):
        T[i].append(l)

S.sort()
T.sort()

for i in range(w):
    if S[i] != T[i]:
        exit(print('No'))

print('Yes')
