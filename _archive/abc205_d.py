from bisect import bisect_left, bisect_right
n, q = map(int, input().split())
A = [0] + list(map(int, input().split()))

K = [int(input()) for _ in range(q)]

for i, k in enumerate(K):
    print(i + 1, bisect_right(A, k))
