n, m = map(int, input().split())
ans = 0
num = ["a"] * n
for _ in range(m):
    s, c = map(int, input().split())
    if s == 1 and c == 0:
        ans = -1
        break
    if num[s - 1] != "a" and num[s - 1] != c:
        ans = -1
        break
    num[s - 1] = c

numStr = ""

if n == 1 and num[0] == "a":
    numStr = ""
    ans = 0

elif num[0] == "a":
    num[0] = "1"

for l in range(n):
    if num[l] == "a":
        numStr += "0"
    else:
        numStr += str(num[l])

print(ans if ans == -1 else numStr)
