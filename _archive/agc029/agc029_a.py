S = list(input())

lenS = len(S)
ans = 0
now = 0

for i in range(10 ** 9):
    if now == len(S) - 1:
        break
    if S[now] == 'B' and S[now + 1] == 'W':
        ans += 1
        S[now] = 'W'
        S[now + 1] = 'B'
        now = max(0, now - 1)
        continue
    now += 1
print(ans)
