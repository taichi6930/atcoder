s = list(input())
ans = ""
for i in range(len(s)):
    if s[i] == "0":
        ans += "0"
    elif s[i] == "1":
        ans += "1"
    else:
        if len(ans) != 0:
            ans = ans[0:len(ans) - 1]

print(ans)
