S = list(input().split("+"))
cnt = 0
for s in S:
    if str(s).find("0") < 0:
        cnt += 1
print(cnt)
