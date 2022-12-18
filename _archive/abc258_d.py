from itertools import accumulate
n, x = map(int, input().split())
A, B = [], []

for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

accA, accB = list(accumulate(A)), list(accumulate(B))

ans = None

for i in range(min(n, x)):
    if ans is None:
        ans = accA[i] + accB[i] + B[i] * (x - i - 1)
        continue
    ans = min(accA[i] + accB[i] + B[i] * (x - i - 1), ans)

print(ans)
