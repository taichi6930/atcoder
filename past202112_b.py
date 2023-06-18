n = int(input())
ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    change = b - a
    for coin in [500, 100, 50, 10, 5, 1]:
        k = int(change / coin)
        if coin == 50 or coin == 5:
            ans += k
        change -= k * coin
print(ans)
