from collections import defaultdict

n, s = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
dic = defaultdict()
dic[0] = ""

for _, ab in enumerate(AB):
    oldK = dic.copy()
    dic = defaultdict()
    for k, v in oldK.items():
        for i, j in enumerate(ab):
            newK = k + j
            newV = f"{v}{'HT'[i]}"
            if s >= newK:
                dic[newK] = newV

if s in dic:
    print("Yes")
    print(dic[s])
    exit()
print("No")
