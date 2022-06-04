k, s = map(int, input().split())
l = [1, 3, 6]

ans = 0

for x in range(k + 1):
    for y in range(x, k + 1):
        z = s - x - y
        if y > z:
            break
        if z > k:
            continue
        ans += l[len(set([x, y, z])) - 1]

print(ans)
