s = input()
i = 0
while len(s) > i:
    i += 2
    sLen = (len(s) - i)
    if s[0:sLen//2] == s[sLen//2:sLen]:
        print(sLen)
        break
