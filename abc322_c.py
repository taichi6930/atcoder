from bisect import bisect_left

n, m = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, n + 1):
    print(A[bisect_left(A, i)] - i)
