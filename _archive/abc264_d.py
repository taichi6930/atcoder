S = list(input())

ans = 0
for i, s in enumerate(list('atcoder')):
    k = S.index(s)
    ans += k
    S = S[:k] + S[k + 1:]

print(ans)
