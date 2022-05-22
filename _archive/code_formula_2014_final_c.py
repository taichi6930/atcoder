S = list(map(str, input().split(' ')))
lis = []

for s in S:
    if s.find('@') < 0:
        continue
    lis += list(map(str, s.split('@')))[1:]

sSet = set(lis)

for s in sorted(list(sSet)):
    if len(s) == 0:
        continue
    print(s)
