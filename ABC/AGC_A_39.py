s = list(input())
k = int(input())
cnt = 0
lenS = len(s)
ans = 0
if lenS == s.count(s[0]):
    ans = (lenS * k // 2)
else:
    for i in range(lenS - 1):
        if s[i] == s[i + 1]:
            s[i + 1] = "1"
            ans += 1
    ans *= k
    if s[0] == s[lenS-1]:
        ans -= k - 1
print(ans)
