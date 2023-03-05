from bisect import bisect_left
from itertools import accumulate
n, m = map(int, input().split())
A = [int(input()) for _ in range(n)]
B = [int(input()) for _ in range(m)]

sum_A = sum(A)

acc_A = [0] + list(accumulate(A + A))

C = [0 for _ in range(n)]
D = [0 for _ in range(2 * n + 1)]
all_C = 0

cnt = 0

for b in B:
    num = b // sum_A
    all_C += num
    temp_b = b - num * sum_A
    bl = bisect_left(acc_A, temp_b + acc_A[cnt])
    D[cnt] += 1
    D[bl - 1] -= 1
    C[bl % n - 1] += temp_b - (acc_A[bl - 1] - acc_A[cnt])
    cnt = (bl) % n

temp = 0
for i in range(len(D)):
    temp += D[i]
    C[i % n] += A[i % n] * temp
for i in range(n):
    print(C[i])
