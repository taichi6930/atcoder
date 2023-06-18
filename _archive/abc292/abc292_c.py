n = int(input())
ans = 0
l = [0]*(n + 1)
for x in range(1, n + 1):
    for y in range(x, n // x + 1):
        if x * y > n:
            continue
        l[x * y] += 1 if x == y else 2

for i in range(1, n):
    ans += l[i] * l[n - i]
print(ans)
