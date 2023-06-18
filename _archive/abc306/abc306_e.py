import heapq

n, k, q = map(int, input().split())
XY = [list(map(int, input().split())) for i in range(q)]

A = [0] * n

sumB = 0
B = A[:k]
heapq.heapify(B)
print(B)


# for i, [x,y] in enumerate(XY):
