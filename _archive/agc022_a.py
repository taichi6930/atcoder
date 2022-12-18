S = list(input())
alphaList = list("abcdefghijklmnopqrstuvwxyz")

if len(S) < 26:
    for alpha in alphaList:
        if alpha in S:
            continue
        exit(print(''.join(S + [alpha])))

for i in range(26):
    if alphaList[i] != S[i]:
        pass
