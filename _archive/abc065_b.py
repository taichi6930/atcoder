n = int(input())
A = [int(input()) - 1 for _ in range(n)]
setA = set([0])

k = 0
for i in range(n + 1):
    k = A[k]
    if k in setA:
        exit(print(-1))
    if k == 1:
        exit(print(i + 1))
    setA.add(k)
