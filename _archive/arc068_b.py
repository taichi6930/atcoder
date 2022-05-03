from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cA = Counter(A)


cA[5] -= 1
print(cA)
