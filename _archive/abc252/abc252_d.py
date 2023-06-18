from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cA = Counter(A)

k1 = (n * (n - 1) * (n - 2)) // 6

for i, key in enumerate(list(cA.keys())):
    cANum = cA[key]
    if cANum >= 3:
        k1 -= (cANum * (cANum - 1) * (cANum - 2)) // 6

    if cANum >= 2:
        k1 -= (cANum * (cANum - 1)) // 2 * (n - cANum)


print(k1)
