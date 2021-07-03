n = int(input())
a = [int(input()) for _ in range(n)]
ans = -1
swi = 1
for i in range(n):
    swi = a[swi - 1]
    if swi == 2:
        ans = i + 1
        break
print(ans)
