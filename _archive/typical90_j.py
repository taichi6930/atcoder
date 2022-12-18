from itertools import accumulate
n = int(input())
C = [[0] * n, [0] * n]

for i in range(n):
    c, p = map(int, input().split())
    C[c - 1][i] = p

C1 = [0] + list(accumulate(C[0]))
C2 = [0] + list(accumulate(C[1]))

q = int(input())

for _ in range(q):
    l, r = map(int, input().split())
    print(C1[r] - C1[l - 1], C2[r] - C2[l - 1])
