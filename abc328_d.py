S = input()
lenS = len(S)
now = 0

while True:
    s = S[now : now + 3]
    # print(f"now: {now},S: {S},s: {s}")
    if len(s) < 3:
        break
    if s == "ABC":
        S = S[:now] + S[now + 3 :]
        lenS -= 3
        now = max(-1, now - 3)
    now += 1
print(S)
