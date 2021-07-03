n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = "No"

sumab = 0
for i in range(n):
    sumab += a[i] * b[i]

if sumab == 0:
    ans = "Yes"
print(ans)
