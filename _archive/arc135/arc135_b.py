n = int(input())
S = list(map(int, input().split()))
A = [0 for _ in range(n + 2)]

for i in range(n - 1):
    p = sum(A[i: i + 3])
    q = (A[i + 2] + S[i] - p)
    if q < 0:
        A[i + 3] += q
        A[i] += q
        A[i - 1] -= q
        continue
    A[i + 2] = q
A[-1] = S[-1] - A[-2] - A[-3]


def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


if min(A) < 0:
    print('No')
else:
    print('Yes')
    print(' '.join(int2strWithArray(A)))
