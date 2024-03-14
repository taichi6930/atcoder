from bisect import bisect_left

n = int(input())
X = sorted(list(map(int, input().split())))
k = bisect_left(X, 0)
S = list()

S += (X[:k][-3:] + X[:k][:3]) if len(X[:k]) >= 6 else X[:k]
S += (X[k:][-3:] + X[k:][:3]) if len(X[k:]) >= 6 else X[k:]
S.sort()

ANS = []

lenS = len(S)
for i in range(lenS - 2):
    for j in range(i + 1, lenS - 1):
        for k in range(j + 1, lenS):
            ANS.append((S[i] + S[j] + S[k]) / (S[i] * S[j] * S[k]))

print(sorted(ANS)[0])
print(sorted(ANS)[-1])
