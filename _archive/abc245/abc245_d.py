def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


n, m = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
B = [None for _ in range(m + 1)]

for i in range(m + 1):
    q = C[n + m - i]
    for j in range(i):
        aNum = n - 1 - j
        bNum = m - i + j + 1
        if 0 > aNum or aNum > n or 0 > bNum or bNum > m:
            break
        q -= A[aNum] * B[bNum]
    B[m - i] = q // A[-1]
print(' '.join(int2strWithArray(B)))
