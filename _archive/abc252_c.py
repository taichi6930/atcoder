def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


n = int(input())
S = [str2intWithArray(list(input())) for _ in range(n)]
T = [[] for _ in range(10)]

for s in S:
    for i in range(10):
        T[i].append(s[i])

ANS = [0 for _ in range(10)]

for i in range(10):
    for j in range(10):
        cnt = T[j].count(i)
        if cnt == 0:
            continue
        ANS[i] = max(ANS[i], (cnt - 1) * 10 + j)

print(min(ANS))
