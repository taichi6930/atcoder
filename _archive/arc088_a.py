x, y = map(int, input().split())
ans = 1

for i in range(1, 100):
    x *= 2
    if x > y:
        break
    ans += 1

print(ans)
