n = int(input())
a, b = [list(map(int, input().split())) for _ in range(2)]
bSum = 0
for i in range(n):
    if a[i] >= b[i]:
        bSum += b[i]
        a[i] -= b[i]
    elif a[i] + a[i + 1] >= b[i]:
        bSum += b[i]
        a[i + 1] -= b[i] - a[i]
        a[i] = 0
    else:
        bSum += a[i] + a[i + 1]
        a[i + 1] = 0

print(bSum)
