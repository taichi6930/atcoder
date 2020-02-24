s = input()
cnt = 0
lenS = len(s)

for i in range(lenS//2):
    if s[i] != s[lenS - i - 1]:
        cnt += 1
    if lenS - 2 * i - 1 <= 1:
        break

print(cnt)
