S = list(input())
k = int(input())

alphaList = list("abcdefghijklmnopqrstuvwxyz")
alphaDic = {alpha: (0 if alpha == 'a' else 26 - i) for i,
            alpha in enumerate(alphaList)}

for i, s in enumerate(S):
    if k < alphaDic[s]:
        continue
    k -= alphaDic[s]
    S[i] = 'a'

S[-1] = alphaList[(k + alphaList.index(S[-1])) % 26]
print(''.join(S))
