a, b, x = map(int, input().split())
k = (b - ((a//x) * x)) // x
print(k + 1 if b % x == 0 else k)
