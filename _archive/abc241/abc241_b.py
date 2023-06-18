import collections

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cA = collections.Counter(A)
cB = collections.Counter(B)

if len(set(cB.keys()) - set(cA.keys())) > 0:
    print('No')
    exit()

for i in cA.keys():
    if cA[i] < cB[i]:
        print('No')
        exit()

print('Yes')
