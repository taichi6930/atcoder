n, k = map(int, input().split())
A = sorted(list(map(int, input().split())))
print(min([A[i + n - k - 1] - A[i] for i in range(k + 1)]))
