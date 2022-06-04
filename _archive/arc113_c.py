from collections import Counter
S = list(input())[::-1]
ans = 0
sDic = Counter()
sDic[S[0]] = 1

for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        sDic[S[i]] += 1
        continue
    ans += i - sDic[S[i]]
    sDic.clear()
    sDic[S[i]] = i + 1

print(ans)
