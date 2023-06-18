# いもす法
n, C = map(int, input().split())
costDic = {}
ans = 0

for i in range(n):
    a, b, c = map(int, input().split())
    if not a in costDic:
        costDic[a] = 0
    costDic[a] += c
    if not b + 1 in costDic:
        costDic[b + 1] = 0
    costDic[b + 1] -= c

costDicKeys = sorted(list(costDic.keys()))

k = 0

for i in range(len(costDicKeys) - 1):
    k += costDic[costDicKeys[i]]
    ans += min(k, C) * (costDicKeys[i + 1] - costDicKeys[i])

print(ans)
