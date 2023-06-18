n, k, x, y = [int(input()) for _ in range(4)]
sum = 0
print(n*x if n-k <= 0 else k*x + (n-k)*y)
