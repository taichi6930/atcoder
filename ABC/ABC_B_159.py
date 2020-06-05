s = input()
n = len(s)
sf = s[0:(n-1)//2]
sr = s[::-1][0:(n-1)//2]
print('YNeos'[not(s == s[::-1] and sf == sf[::-1] and sr == sr[::-1])::2])