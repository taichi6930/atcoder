from collections import Counter
n, k = map(int, input().split())
A = list(map(int, input().split()))
cA = Counter(A)
cA[0] = min(cA[0], k)

num = n
ans = 0

for i in range(10 ** 9):
    nu = cA[i]
    ans += max((num - cA[i]), 0) * i
    num = min(nu, num)
    if num == 0:
        break
print(ans)
