s = input()
t = input()

for i in range(len(s) - len(t) + 1):
    if t == s[i: i + len(t)]:
        exit(print('Yes'))
print('No')
