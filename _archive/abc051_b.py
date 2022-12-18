k, s = map(int, input().split())
ans = 0
for x in range(k + 1):
    for y in range(x, k + 1):
        z = s - x - y
        if y > z:
            break
        if z > k:
            continue
        if x == y and y == z:
            ans += 1
            continue
        if x == y or y == z:
            ans += 3
            continue
        ans += 6

print(ans)
