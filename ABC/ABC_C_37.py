n, k = map(int, input().split())
x, y = min(k, n-k+1), max(k, n-k+1)
a = list(map(int, input().split()))
print(sum(a[i] * min(i+1, n-i, x) for i in range(n)))
