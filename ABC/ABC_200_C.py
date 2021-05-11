import collections

n = int(input())
A = list(map(int, input().split()))
B = [None] * n

for i in range(n):
    B[i] = A[i] % 200

counter = collections.Counter(B)
c = list(counter.values())
# print(list(counter.values()))

sumC = 0

for j in range(len(c)):
    k = c[j]
    sumC += k * (k-1) // 2
print(sumC)
