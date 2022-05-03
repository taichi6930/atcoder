n = int(input())
ans = 100 * (n // 10) + min(100, (n - (n // 10) * 10) * 15)
print(ans)
