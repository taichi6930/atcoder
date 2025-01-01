from itertools import combinations
from collections import defaultdict


a, b, c, d, e = map(int, input().split())
values = [a, b, c, d, e]
labels = ["A", "B", "C", "D", "E"]

ansDict = defaultdict(list)

for r in range(1, 6):
    for comb in combinations(range(5), r):
        st = "".join(labels[i] for i in comb)
        ans = sum(values[i] for i in comb)
        ansDict[ans].append(st)

sorted_ansDict = dict(sorted(ansDict.items(), reverse=True))

for keys in sorted_ansDict:
    sorted_ansDict[keys].sort()
    for key in sorted_ansDict[keys]:
        print(key)
