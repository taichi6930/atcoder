from collections import Counter

n = int(input())
A = list(map(int, input().split()))
cS = Counter()
for i in range(n):
    for j in range(i, n):
        cS[sum(list(map(lambda x: int(x), list(str(A[i] + A[j])))))] += (
            1 if i == j else 2
        )
print(sum([x * y for (x, y) in zip(cS.keys(), cS.values())]))
