S = input()
T = input()

setT = set()

for i in range(len(T)):
    a = S[len(S) - len(T) + i]
    b = T[i]
    if a == '?' or b == '?':
        continue
    if a == b:
        continue
    setT.add(i)

print('Yes' if len(setT) == 0 else 'No')

for j in range(len(T)):
    b = S[j]
    c = T[j]
    if b == '?' or c == '?':
        setT.discard(j)
    elif b == c:
        setT.discard(j)
    else:
        setT.add(j)
    print('Yes' if len(setT) == 0 else 'No')
