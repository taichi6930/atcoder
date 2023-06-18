S = list(map(str, input().split()))
SLenList = [len(s) for s in S]
n = int(input())
T = [input() for _ in range(n)]
TLenList = [len(t) for t in T]

for i in range(len(T)):
    for j in range(len(S)):
        if SLenList[j] != TLenList[i]:
            continue
        swi = True
        for ss in range(len(S[j])):
            if T[i][ss] == '*':
                continue
            if T[i][ss] != S[j][ss]:
                swi = False
                break
        if swi:
            S[j] = '*' * SLenList[j]

print(' '.join(S))
