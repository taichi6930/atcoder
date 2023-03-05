from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cA = Counter(A)

sumcA = sum([value * (value - 1) // 2 for value in cA.values()])

for a in A:
    print(sumcA - cA[a] + 1)
