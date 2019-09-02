s, t = [list(input()) for _ in range(2)]
ans = 0
for i in range(3):
    if s[i] == t[i]:
        ans += 1
print(ans)
