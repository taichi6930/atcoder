n, k = map(int, input().split())
h = sorted([int(input()) for _ in range(n)])
print(min(h[k+i-1]-h[i] for i in range(n-k+1)))
