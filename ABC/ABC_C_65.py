def prod(n):
    x = 1
    for i in range(1, n+1):
        x *= i
        x %= (10 ** 9 + 7)
    return x


n, m = map(int, input().split())
n, m = min(n, m), max(n, m)
minusNM = m - n
ans = 0
if minusNM == 0:
    ans = 2 * prod(n) ** 2
elif minusNM == 1:
    ans = prod(n) ** 2 * m
print(ans % (10 ** 9 + 7))
