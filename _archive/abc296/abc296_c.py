n, x = map(int, input().split())
A = list(map(int, input().split()))
setA = set(A)

for a in setA:
    if a - x in setA:
        exit(print('Yes'))
print('No')
