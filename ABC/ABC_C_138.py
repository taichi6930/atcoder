n = int(input())
v = sorted(map(int, input().split()), reverse=True)
sum = v[n - 1] / 2 ** (n)
for i in range(n):
    sum += v[i] / 2 ** (i + 1)
print(sum)
