S = list(input())

numList = list("0123456789")

ans = ""

for s in S:
    if s in numList:
        ans += s

print(ans)
