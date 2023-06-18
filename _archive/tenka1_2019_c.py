from collections import Counter
n = int(input())
S = list(input())

for i in range(n):
    if len(S) == 0:
        break
    if S[-1] != '#':
        break
    S.pop()

S = S[::-1]

for i in range(n):
    if len(S) == 0:
        break
    if S[-1] != '.':
        break
    S.pop()

S = S[::-1]

cS = Counter(S)
print(min(cS['#'], cS['.']))
