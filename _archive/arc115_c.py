def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


n = int(input())
A = [False] + [None] * (n - 1)

for i in range(n):
    if A[i] == False:
        continue
    A[i] = True
    for j in range(2, n):
        if (i + 1) * j - 1 >= n:
            break
        A[(i + 1) * j - 1] = False
A[1] = False

trueNum = 2
falseNum = 1

B = []

for i in range(n):
    if A[i]:
        B.append(trueNum)
        trueNum += 1
    else:
        B.append(falseNum)
        falseNum += 1
print(' '.join(int2strWithArray(B)))
