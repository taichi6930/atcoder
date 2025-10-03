d = int(input())
ans = d

for x in range(10**7):
    if x**2 - d > 0:
        break
    y0 = int((d - x**2) ** 0.5)
    for y in range(max(y0, 0), y0 + 3):
        ans = min(ans, abs(x**2 + y**2 - d))
print(ans)
