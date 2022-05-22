from collections import Counter
n = int(input())
cS = Counter()
scoreDic = {}

for i in range(n):
    [s, t] = map(str, input().split())
    t = int(t)
    cS[s] += 1
    if cS[s] > 1:
        continue
    if not t in scoreDic:
        scoreDic[t] = []
    scoreDic[t].append(i + 1)

print(min(scoreDic[max(scoreDic.keys())]))
