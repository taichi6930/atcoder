R, G, B, n = map(int, input().split())
RGB1 = max(R, G, B)
RGB3 = min(R, G, B)
RGB2 = (R + G + B) - (RGB1 + RGB3)
ans = 0
for i in range(10 ** 9):
    if RGB1 * i > n:
        break
    for j in range(10 ** 9):
        if RGB1 * i + RGB2 * j > n:
            break
        k = n - (RGB1 * i + RGB2 * j)
        if k % RGB3 != 0:
            continue
        ans += 1

print(ans)
