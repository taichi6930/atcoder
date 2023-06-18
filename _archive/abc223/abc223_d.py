n, m = map(int, input().split())
beforeAB = [[] for _ in range(n)]
afterAB = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    beforeAB[b - 1].append(a)
    afterAB[a - 1].append(b)

print(beforeAB, afterAB)
