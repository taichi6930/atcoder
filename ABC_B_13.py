a, b = [int(input()) for _ in range(2)]
ans = abs(a - b)
print(ans) if (ans < 5) else print(10 - ans)
