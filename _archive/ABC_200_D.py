import collections
n = int(input())
A = list(map(int, input().split()))
B = [None] * n

for i in range(n):
    B[i] = A[i] % 200

c = collections.Counter(B)

if c.most_common()[0][1] > 1:
    k = B.index(c.most_common()[0][0])
    print("Yes")
    print(1, k + 1)
    print(1, B[k + 1: n].index(c.most_common()[0][0]) + k + 2)
