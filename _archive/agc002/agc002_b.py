n, m = map(int, input().split())
ans = set([1])

for i in range(m):
    x, y = map(int, input().split())
    if y in ans:
        continue
    if x in ans:
        ans.add(y)

print(ans)
