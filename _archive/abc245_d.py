n, m = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
B = [0 for _ in range(n + m)]

for i in range((n + m + 1) // 2):

    q = C[i]
    for j in range(i):
        q -= B[j] * A[i - j]
    B[i] = q // A[0]
    print(i, q // A[0])

    l = - (i + 1)

    r = C[l]
    print("r:", r)
    for j in range(i):
        r -= B[(n - 1) - j] * A[(m - 1) - i + j]
        print("r:", r, (n - 1) - j, (m - 1) - i + j)
    B[l] = r // A[-1]
    print(l + n + m, r // A[-1])


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


print(' '.join(int2strWithArray(B)))
