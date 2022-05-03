n, k = map(int, input().split())

if k == 0:
    print(n ** 2)
    exit()


ans = 0

for b in range(k, n + 1):
    i = b - (k + 1) + 1
    p = n // b
    q = n - p * b
    ans += p * i + max(0, q - k + 1)

print(ans)
