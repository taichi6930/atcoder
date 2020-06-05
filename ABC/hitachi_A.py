s = input()
ans = "No"
if len(s) != 1:
    for i in range(len(s) - 2):
        if s[i:i+2] == "hi":
            ans = "Yes"
            break
    if s[len(s)-2:len(s)] == "hi":
        ans = "Yes"

print(ans)
