n = int(input())
A = [1]


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


for i in range(n):
    print(' '.join(int2strWithArray(A)))
    newA = [1]
    for j in range(len(A) - 1):
        newA.append(A[j] + A[j + 1])
    newA += [1]
    A = newA
