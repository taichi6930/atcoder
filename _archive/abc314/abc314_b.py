n = int(input())
listA = []
for _ in range(n):
    __ = int(input())
    listA.append(list(map(int, input().split())))

X = int(input())

from collections import defaultdict

ansDict = defaultdict(list)

for i, A in enumerate(listA):
    if X in A:
        ansDict[len(A)].append(i + 1)

if len(ansDict) == 0:
    print(0)
    exit(print(""))

ansList = ansDict[min(ansDict.keys())]
print(len(ansList))
print(*ansList)
