n, l = map(int, input().split())
ans = 0
a = [0] * (n + 1)

for i in range(n + 1):
    if i < l:
        a[i] = 1
        continue
    a[i] = (a[i - 1] + a[i - l]) % (10 ** 9 + 7)

print(a[- 1])
