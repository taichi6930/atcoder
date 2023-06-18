n = int(input())
ans = n * 1

for i in range(100):
    b = 69 - i
    a = int(n / (2 ** b))
    c = n - a * 2 ** b
    ans = min(ans, a + b + c)

print(ans)
