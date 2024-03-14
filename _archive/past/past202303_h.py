from collections import Counter

n = int(input())
A = list(map(int, input().split()))
cA = Counter(A)
keys = sorted(cA.keys())
for key in keys:
    minCA = min(cA[key], cA[key + 1], cA[key + 2])
    cA[key] -= minCA
    cA[key + 1] -= minCA
    cA[key + 2] -= minCA
print(sum(cA.values()))
