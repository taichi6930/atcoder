n, k, q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for kk in L:
    k = kk - 1
    if A[k] == n:
        continue
    if A[k] + 1 in A:
        continue
    A[k] = A[k] + 1


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


print(' '.join(int2strWithArray(A)))
