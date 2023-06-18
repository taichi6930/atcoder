from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cA = Counter(A)

keys = sorted(list(cA.keys()), reverse=True)
ansList = []

for key in keys:
    if cA[key] >= 4:
        ansList.append(key)
    if cA[key] >= 2:
        ansList.append(key)

print(ansList[0] * ansList[1] if len(ansList) >= 2 else 0)
