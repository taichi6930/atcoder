n, k = map(int, input().split())
h = sorted([int(input()) for _ in range(n)])
print(min(h[k-1]-h[0], h[n-1]-h[n-k]))
