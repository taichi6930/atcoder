from itertools import accumulate  # 累積和を求めるときに使う

n, k = map(int, input().split())
A = list(map(int, input().split()))
AA = A[:k]
minA = min(AA)
B = [AA[-1]]
for i in range(k - 1):
    B.append(min(B[-1], AA[k - i - 2]))

B = B[::-1]

ans = 10 ** 10
swi = False
st = 0

for i in range(k, n):
    if A[i] <= minA:
        continue
    if k <= st:
        break
    for j in range(n):
        if k <= st:
            break
        if A[i] > B[st]:
            swi = True
            ans = min(ans, i - st)
            st += 1
            continue
        break

print(ans if swi else -1)
