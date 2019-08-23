n, x = map(int, input().split())
a = list(map(int, input().split()))
k = (('{:0' + str(n) + 'b}').format(x))[::-1]
sum = 0
for i in range(n):
    sum += int(k[i]) * a[i]
print(sum)
