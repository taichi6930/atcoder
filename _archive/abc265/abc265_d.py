from itertools import accumulate

n, p, q, r = map(int, input().split())
A = list(map(int, input().split()))
accA = [0] + list(accumulate(A))
setA = set(accA)
for i, a in enumerate(accA):
    if not p + q + r + a in setA:
        continue
    if not p + q + a in setA:
        continue
    if not p + a in setA:
        continue

    exit(print('Yes'))
print('No')
