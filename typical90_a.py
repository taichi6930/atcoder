import math
from itertools import accumulate  # 累積和を求めるときに使う

n, l = map(int, input().split())
k = int(input())

A = [0] + list(map(int, input().split())) + [l]
ans = 0
r = l

for i in range(10 ** 10):
    b = 0
    cnt = 0
    for j in range(n + 1):
        ls = A[j + 1] - A[b]
        if r <= ls:
            b = j + 1
            cnt += 1

    if cnt >= k + 1:
        ans = max(ans, r)

    p = max(math.ceil(l // 2 ** (i + 1)), 1)

    r = r + p if cnt >= k + 1 else r -= p

    if r == ans:
        break


print(ans)
