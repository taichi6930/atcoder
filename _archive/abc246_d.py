n = int(input())
ans = 10 ** 18
b = int(n ** (1 / 3) + 2)

for a in range(10 ** 18 + 1):
    if a ** 2 > n:
        break
    if b < a:
        break
    for c in range(10 ** 18 + 1):
        if b < a:
            break
        k = a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3
        if n > k:
            break
        ans = min(ans, k)
        b -= 1


print(ans)
