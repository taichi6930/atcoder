from bisect import bisect_left

n = int(input())
A = sorted(list(map(int, input().split())))
q = int(input())

num = 0
for i in range(q):
    b = int(input())
    x = bisect_left(A, b)
    if x == 0:
        print(A[0] - b)
    elif x == n:
        print(b - A[-1])
    else:
        print(min(b - A[x - 1], A[x] - b))
