n, m = map(int, input().split())
ans = None

for a in range(1, 10 ** 12 + 1):
    b = m // a if m % a == 0 else m // a + 1
    if b < a:
        break
    if b > n:
        continue
    if ans is None:
        ans = a * b
    ans = min(ans, a * b)
print(-1 if ans is None else ans)
