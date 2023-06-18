from collections import Counter, deque
S = list(input())
cS = Counter(S)

ans = ''

alphaList = list("abcdefghijklmnopqrstuvwxyz")

for alpha in alphaList:
    ans += alpha * cS[alpha]

print(ans)
