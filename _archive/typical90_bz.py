from collections import *
n, m = map(int, input().split())
AB = [sorted(list(map(int, input().split()))) for _ in range(m)]

dic = defaultdict(list)
for i, [a, b] in enumerate(AB):
    dic[b].append(a)

print(sum([1 if len(dic[k]) == 1 else 0 for k in list(dic.keys())]))
