n, m = map(int, input().split())
ans = ''
num = 1

for i in range(m):
    num *= n
    if num > 10 ** 9:
        ans += 'x' * (m - i)
        break
    ans += 'o'

print(ans)
