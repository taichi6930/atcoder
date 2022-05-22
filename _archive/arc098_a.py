from collections import Counter
n = int(input())
S = list(input())
cS1 = Counter()
cS2 = Counter(S[1:])

ans = 10 ** 10

for i in range(n - 1):
    ans = min(cS1['W'] + cS2['E'], ans)
    cS1[S[i]] += 1
    cS2[S[i + 1]] -= 1

print(min(cS1['W'] + cS2['E'], ans))
