n, l, r = map(int, input().split())

ans = 0

for i in range(l, r + 1):
    print(bin(i), bin(n), bin(i ^ n))
    if i ^ n < n:
        ans += 1

print(ans)
