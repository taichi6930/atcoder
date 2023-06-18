n = int(input())
ST = []

for _ in range(n):
    x, l = map(int, input().split())
    ST.append([x - l, x + l])

ST.sort(key=lambda x: x[1])

p = -10 ** 20
ans = 0

for i in range(n):
    if ST[i][0] < p:
        continue
    ans += 1
    p = ST[i][1]

print(ans)
