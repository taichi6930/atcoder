n, k = map(int, input().split())
cnt = 0

for i in range(10 ** 12):
    if n < k * 10 ** i:
        break
    cnt += 1

for i in range(10 ** 12):
    if n < int(str(k)[::-1]) * 10 ** i:
        break
    cnt += 1

print(cnt)
