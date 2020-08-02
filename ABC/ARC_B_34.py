n = int(input())
s = [0] * 155
cnt = 0
for i in range(max(1, n - 155), n):
    if i + sum([int(a) for a in list(str(i))]) == n:
        s[cnt] = i
        cnt += 1
print(cnt)
for k in s:
    if k == 0:
        break
    print(k)
