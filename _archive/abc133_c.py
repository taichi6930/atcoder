l, r = map(int, input().split())
ans = 10 ** 30
for i in range(l, min(l + 2019, r) + 1):
    for j in range(i + 1, min(l + 2019, r) + 1):
        ans = min(i % 2019 * j % 2019, ans)
print(ans)
