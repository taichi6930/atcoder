n = int(input())
S = [input() for _ in range(n)]
if len(set(S)) != n:
    exit(print('No'))
for s in S:
    [a, b] = list(s)
    if not a in ['H', 'D', 'C', 'S']:
        exit(print('No'))
    if not b in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
        exit(print('No'))
print('Yes')
