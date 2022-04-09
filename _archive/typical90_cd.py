mod = 10 ** 9 + 7

l, r = map(int, input().split())
ans = 0

for i in range(20):
    if l > 10 ** (i + 1) - 1:
        continue
    if r < 10 ** i:
        break
    minA = max(10 ** i, l)
    maxA = min(10 ** (i + 1) - 1, r)
    cnt = min(maxA, r) - max(minA, l) + 1
    ans = (ans + ((minA + maxA) * (i + 1) * cnt // 2) % mod) % mod

print(ans)
