n, x = map(int, input().split())
l = list(map(int, input().split()))
d = 0
ans = 1
for i in range(0, n):
    d = d + l[i]
    if d <= x:
        ans += 1

print(ans)
