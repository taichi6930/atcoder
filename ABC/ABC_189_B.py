n, x = map(int, input().split())
ans = -1
sumV = 0
for i in range(n):
    v, p = map(int, input().split())
    sumV += v * p
    if sumV > x * 100:
        ans = i + 1
        break

print(ans)
