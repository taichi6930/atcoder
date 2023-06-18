from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

ADict = defaultdict(list)

for i, a in enumerate(A):
    ADict[a].append(i + 1)

AList = [[k, v[1]] for k, v in ADict.items()]

print(" ".join([str(j[0]) for j in sorted(AList, key=lambda x: x[1])]))
