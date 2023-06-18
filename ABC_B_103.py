s, t = [input() for _ in range(2)]
k = 0
for i in range(len(s)):
    if s[i:len(s)] + s[0:i] == t:
        print("Yes")
        k = 1
        break
if k == 0:
    print("No")
