x, a, d, n = map(int, input().split())
minS = a
maxS = a + d * (n - 1)

# 最小値以下だったら、minSとの差を計算する
if min(minS, maxS) >= x:
    print(min(abs(x - minS), abs(x - maxS)))
    exit()

# 最大値以上だったら、maxとの差を計算する
if max(minS, maxS) <= x:
    print(min(abs(x - minS), abs(x - maxS)))
    exit()

nn = 1 + (x - a) / d

ans = 10 ** 11
for i in range(max(int(nn) - 2, 1), min(int(nn) + 2, n + 1)):
    ans = min(abs(x - (a + d * (i - 1))), ans)

print(ans)
