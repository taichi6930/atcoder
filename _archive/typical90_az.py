n = int(input())
ans = 1
w = 10 ** 9 + 7
for i in range(n):
    a = sum(list(map(int, input().split())))
    ans = (ans * a % w) % w
print(ans)
