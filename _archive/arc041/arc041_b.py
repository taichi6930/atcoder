def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


M, N = map(int, input().split())
B = [str2intWithArray(list(input())) for _ in range(M)]
A = [[0 for _ in range(N)] for _ in range(M)]

for m in range(1, M - 1):
    for n in range(1, N - 1):
        num = min(B[m - 1][n], B[m + 1][n], B[m][n - 1], B[m][n + 1])
        A[m][n] += num
        B[m - 1][n] -= num
        B[m + 1][n] -= num
        B[m][n - 1] -= num
        B[m][n + 1] -= num

for a in A:
    print(''.join(int2strWithArray(a)))
