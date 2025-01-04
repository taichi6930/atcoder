S = input()

ans = 0
while True:
    if len(S) < 2:
        ans += 1
        break
    S = S[(2 if S.startswith("00") else 1) :]
    ans += 1
print(ans)
